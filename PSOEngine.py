import numpy as np
from pyswarm import pso  # PSO için hazır kütüphane
from AnonymizationPipeline import AnonymizationPipeline  # Mevcut anonimleştirme modülü


class PSOEngine:
    def __init__(self, data_path, hierarchy_folder, quasi_identifiers, sensitive_attribute):
        self.data_path = data_path
        self.hierarchy_folder = hierarchy_folder
        self.quasi_identifiers = quasi_identifiers
        self.sensitive_attribute = sensitive_attribute
        self.pipeline = AnonymizationPipeline(data_path, hierarchy_folder)

    def objective_function(self, params):
        """
        PSO'nun minimize etmeye çalıştığı amaç fonksiyonu.
        Parametreler:
            - params: [k, l, t] (optimize edilen anonimlik metrikleri)
        """
        k, l, t = params
        try:
            # Anonimleştirme işlemini çalıştır
            anonymized_data = self.pipeline.run(
                identifiers=["race"],
                quasi_identifiers=self.quasi_identifiers,
                sensitive_attribute=self.sensitive_attribute,
                k=int(k),
                l=int(l),
                t=float(t),
                suppression_level=10,  # Sabit baskılama oranı
            )

            # Bilgi kaybını hesapla
            suppression_rate = self.pipeline.calculate_suppression_rate(anonymized_data)
            ncp = self.pipeline.calculate_ncp(anonymized_data)

            # Fayda ve risk metriklerini birleştirerek tek bir hedef oluştur
            objective_value = suppression_rate + ncp  # Daha düşük değerler daha iyidir
            return objective_value

        except Exception as e:
            print(f"Hata oluştu: {e}")
            return np.inf  # Eğer bir hata oluşursa çok kötü bir skor döndür

    def optimize(self,k_range,l_range,t_range):
        """
        PSO algoritmasını çalıştırarak en iyi sonucu bul.
        """
        # Alt ve üst sınırları belirle
        lower_bounds = [k_range[0], l_range[0], t_range[0]]
        upper_bounds = [k_range[1], l_range[1], t_range[1]]

        # PSO'yu çalıştır
        best_params, best_score = pso(
            self.objective_function,
            lb=lower_bounds,
            ub=upper_bounds,
            swarmsize=10,  # Parçacık sayısı
            maxiter=20,    # Maksimum iterasyon sayısı
        )

        print(f"En iyi parametreler: k={int(best_params[0])}, l={int(best_params[1])}, t={float(best_params[2])}")
        print(f"En iyi skor: {best_score}")

        return {
            "k": int(best_params[0]),
            "l": int(best_params[1]),
            "t": float(best_params[2]),
            "score": best_score,
        }
