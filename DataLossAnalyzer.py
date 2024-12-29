import pandas as pd    

class DataLossAnalyzer:
    def __init__(self, original_data, anonymized_data):
        self.original_data = original_data
        self.anonymized_data = anonymized_data

    def calculate_suppression_rate(self):
        original_length = len(self.original_data)
        anonymized_length = len(self.anonymized_data)
        return (original_length - anonymized_length) / original_length

    def calculate_ncp(self):
        ncp_total = 0
        for col in self.original_data.columns:
            if pd.api.types.is_numeric_dtype(self.original_data[col]):
                try:
                    original_range = self.original_data[col].max() - self.original_data[col].min()
                    anonymized_range = self.anonymized_data[col].max() - self.anonymized_data[col].min()
                    ncp_total += (anonymized_range / original_range) if original_range != 0 else 0
                except Exception:
                    continue
            elif self.original_data[col].dtype == "object":
                try:
                    original_unique = len(self.original_data[col].dropna().unique())
                    anonymized_unique = len(self.anonymized_data[col].dropna().unique())
                    ncp_total += (anonymized_unique / original_unique) if original_unique != 0 else 0
                except Exception:
                    continue
        ncp_total /= len(self.original_data.columns)
        return ncp_total
