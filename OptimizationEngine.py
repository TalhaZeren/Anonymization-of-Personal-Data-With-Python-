import pandas as pd
from DataLossAnalyzer import DataLossAnalyzer
from AnonymityAnalyzer import AnonymityAnalyzer
from Anonymizer import Anonymizer

class OptimizationEngine:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def optimize(self, quasi_identifiers, sensitive_attribute, hierarchies, k_values, l_values, t_values):
        results = []
        best_score = float('-inf')  # Başlangıç için en düşük skor
        best_result = None

        # Ağırlıklar: Literatürden önerilen değerler
        weights = {
            "k": 0.3,  # k-Anonimlik ağırlığı
            "l": 0.2,  # l-Diversity ağırlığı
            "t": 0.2,  # t-Closeness ağırlığı
            "ncp": -0.2,  # NCP (negatif çünkü minimize edilmeli)
            "suppression_rate": -0.1  # Suppression rate (negatif çünkü minimize edilmeli)
        }

        for k in k_values:
            for l in l_values:
                for t in t_values:
                    # Her kombinasyon için anonimleştirme işlemi
                    anonymizer = Anonymizer(self.data_processor.get_data(), self.data_processor.get_hierarchies())
                    data_anon = anonymizer.apply_k_anonymity([], quasi_identifiers, k, 50)
                    data_anon = anonymizer.apply_l_diversity([], quasi_identifiers, sensitive_attribute, k, l, 50)
                    data_anon = anonymizer.apply_t_closeness([], quasi_identifiers, sensitive_attribute, k, t, 50)

                    # Anonimlik Analizi
                    analyzer = AnonymityAnalyzer(self.data_processor.get_data(), data_anon, quasi_identifiers, sensitive_attribute)
                    k_result = analyzer.calculate_k_anonymity()
                    l_result = analyzer.calculate_l_diversity()
                    t_result = analyzer.calculate_t_closeness()

                    # Bilgi Kaybı Analizi
                    loss_analyzer = DataLossAnalyzer(self.data_processor.get_data(), data_anon)
                    suppression_rate = loss_analyzer.calculate_suppression_rate()
                    ncp = loss_analyzer.calculate_ncp()

                    # Fayda-risk skorunu hesapla (literatüre uygun formül)
                    score = (
                        weights["k"] * k_result +
                        weights["l"] * l_result -
                        weights["t"] * t_result +
                        weights["ncp"] * ncp +
                        weights["suppression_rate"] * suppression_rate
                    )

                    # En iyi skoru kaydet
                    if score > best_score:
                        best_score = score
                        best_result = {
                            "k": k,
                            "l": l,
                            "t": t,
                            "k_result": k_result,
                            "l_result": l_result,
                            "t_result": t_result,
                            "suppression_rate": suppression_rate,
                            "ncp": ncp,
                            "score": score
                        }

                    # Tüm sonuçları listeye ekle
                    results.append({
                        "k": k,
                        "l": l,
                        "t": t,
                        "k_result": k_result,
                        "l_result": l_result,
                        "t_result": t_result,
                        "suppression_rate": suppression_rate,
                        "ncp": ncp,
                        "score": score
                    })

        # En iyi sonucu ve tüm kombinasyonları döndür
        return best_result, results
