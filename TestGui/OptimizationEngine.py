import pandas as pd
import numpy as np
from pyswarms.single.global_best import GlobalBestPSO

class OptimizationEngine:
    def __init__(self, data, hierarchies, quasi_identifiers, sensitive_attribute, identifiers=None):
        """
        :param data: Orijinal veri seti (Pandas DataFrame).
        :param hierarchies: Quasi-identifier sütunlarının hiyerarşi bilgileri (sözlük formatında).
        :param quasi_identifiers: Quasi-identifier sütunlarının listesi.
        :param sensitive_attribute: Hassas öznitelik.
        :param identifiers: Identifier sütunları (örneğin, race).
        """
        self.data = data
        self.hierarchies = hierarchies
        self.quasi_identifiers = quasi_identifiers
        self.sensitive_attribute = sensitive_attribute
        self.identifiers = identifiers if identifiers else []

    def apply_k_anonymity(self, data, k):
        for column in self.quasi_identifiers:
            unique_vals = data[column].unique()
            group_size = max(1, len(unique_vals) // k)
            data[column] = data[column].apply(
                lambda x: f"group_{x // group_size * group_size}" if pd.api.types.is_numeric_dtype(data[column]) else f"group_{x}"
            )
        return data

    def apply_l_diversity(self, data, l):
        equivalence_classes = data.groupby(self.quasi_identifiers)
        valid_rows = []
        for _, group in equivalence_classes:
            if len(group[self.sensitive_attribute].unique()) >= l:
                valid_rows.append(group)
        return pd.concat(valid_rows) if valid_rows else pd.DataFrame(columns=data.columns)

    def apply_t_closeness(self, data, t):
        global_distribution = data[self.sensitive_attribute].value_counts(normalize=True)
        equivalence_classes = data.groupby(self.quasi_identifiers)
        valid_rows = []
        for _, group in equivalence_classes:
            local_distribution = group[self.sensitive_attribute].value_counts(normalize=True)
            emd = np.abs(global_distribution - local_distribution).sum()
            if emd <= t:
                valid_rows.append(group)
        return pd.concat(valid_rows) if valid_rows else pd.DataFrame(columns=data.columns)

    def suppression_rate(self, original_data, anonymized_data):
        return (len(original_data) - len(anonymized_data)) / len(original_data)

    def calculate_ncp(self, original_data, anonymized_data):
        ncp = 0
        for column in self.quasi_identifiers:
            unique_orig = len(original_data[column].unique())
            unique_anon = len(anonymized_data[column].unique())
            ncp += (unique_anon / unique_orig) if unique_orig != 0 else 0
        return ncp / len(self.quasi_identifiers)

    def fayda_risk_score(self, params):
        """
        PSO ile kullanılan optimizasyon fonksiyonu.
        :param params: [k, l, t] değerlerinden oluşan bir dizi.
        :return: Fayda-risk skoru (negatif döner çünkü minimize edilmeli).
        """
        k, l, t = map(int, params[:2]) + [float(params[2])]

        # Anonimleştirme adımları
        anonymized_data = self.apply_k_anonymity(self.data.copy(), k)
        anonymized_data = self.apply_l_diversity(anonymized_data, l)
        anonymized_data = self.apply_t_closeness(anonymized_data, t)

        # Veri boşsa yüksek maliyet döndür
        if anonymized_data.empty:
            return float("inf")  # Çok yüksek maliyet

        # Fayda-risk metrikleri
        supp_rate = self.suppression_rate(self.data, anonymized_data)
        ncp = self.calculate_ncp(self.data, anonymized_data)

        # Fayda-risk skorunu döndür
        return -1 * (0.3 * k + 0.2 * l - 0.2 * (1 - t) - 0.2 * ncp - 0.1 * supp_rate)

    def optimize(self, k_bounds, l_bounds, t_bounds, n_particles=10, iters=50):
        """
        PSO ile optimize et.
        :param k_bounds: k değerlerinin [min, max] aralığı.
        :param l_bounds: l değerlerinin [min, max] aralığı.
        :param t_bounds: t değerlerinin [min, max] aralığı.
        :param n_particles: PSO parçacık sayısı.
        :param iters: PSO iterasyon sayısı.
        :return: En iyi maliyet ve en iyi parametreler.
        """
        bounds = (np.array([k_bounds[0], l_bounds[0], t_bounds[0]]),
                  np.array([k_bounds[1], l_bounds[1], t_bounds[1]]))
        optimizer = GlobalBestPSO(
            n_particles=n_particles,
            dimensions=3,  # k, l, t için 3 boyut
            options={'c1': 1.5, 'c2': 1.5, 'w': 0.5},
            bounds=bounds
        )
        best_cost, best_pos = optimizer.optimize(self.fayda_risk_score, iters=iters)
        return best_cost, best_pos



