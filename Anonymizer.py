from anjana.anonymity import k_anonymity, l_diversity, t_closeness

# Anonymizer Class
class Anonymizer:
    def __init__(self, data, hierarchies):
        self.data = data
        self.hierarchies = hierarchies

    def apply_k_anonymity(self, identifiers, quasi_identifiers, k, suppression_level):
        return k_anonymity(self.data, identifiers, quasi_identifiers, k, suppression_level, self.hierarchies)

    def apply_l_diversity(self, identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level):
        return l_diversity(self.data, identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level, self.hierarchies)

    def apply_t_closeness(self, identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level):
        return t_closeness(self.data, identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level, self.hierarchies)