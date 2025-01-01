from pycanon import anonymity
from anjana.anonymity.utils import get_transformation

class AnonymityAnalyzer:
    def __init__(self, original_data, anonymized_data, quasi_identifiers, sensitive_attribute):
        self.original_data = original_data
        self.anonymized_data = anonymized_data
        self.quasi_identifiers = quasi_identifiers
        self.sensitive_attribute = sensitive_attribute

    def calculate_k_anonymity(self):
        return anonymity.k_anonymity(self.anonymized_data, self.quasi_identifiers)

    def calculate_l_diversity(self):
        return anonymity.l_diversity(self.anonymized_data, self.quasi_identifiers, [self.sensitive_attribute])

    def calculate_t_closeness(self):
        return anonymity.t_closeness(self.anonymized_data, self.quasi_identifiers, [self.sensitive_attribute])