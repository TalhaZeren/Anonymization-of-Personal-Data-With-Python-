from anjana.anonymity import k_anonymity, l_diversity, t_closeness

class Anonymizer:
    def __init__(self, data, hierarchies : dict):
        self.data = data
        self.hierarchies = hierarchies

    def apply_k_anonymity(self, identifiers, quasi_identifiers, k, suppression_level):
        self.data = k_anonymity(self.data, identifiers, quasi_identifiers, k, suppression_level, self.hierarchies)
        return self.data

    def apply_l_diversity(self, identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level):
        self.data = l_diversity(self.data, identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level, self.hierarchies)
        return self.data

    def apply_t_closeness(self, identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level):
        self.data = t_closeness(self.data, identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level, self.hierarchies)
        return self.data
