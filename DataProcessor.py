import pandas as pd

class DataProcessor:
    def __init__(self, data_path, hierarchy_folder):
        self.data = pd.read_csv(data_path)
        self.hierarchy_folder = hierarchy_folder
        self.hierarchies = {}

    def clean_columns(self, columns_to_strip):
        self.data.columns = self.data.columns.str.strip()
        for col in columns_to_strip:
            if col in self.data.columns and self.data[col].dtype == "object":
                self.data[col] = self.data[col].str.strip()

    def load_hierarchies(self, quasi_identifiers):
        for qi in quasi_identifiers:
            hierarchy_file = f"{self.hierarchy_folder}/{qi}.csv"
            try:
                self.hierarchies[qi] = pd.read_csv(hierarchy_file, header=None, index_col=0).to_dict(orient='list')
            except FileNotFoundError:
                raise FileNotFoundError(f"Hiyerarşi dosyası bulunamadı: {hierarchy_file}")
            except Exception as e:
                raise ValueError(f"Hiyerarşi yüklenirken hata oluştu: {e}")

    def get_data(self):
        return self.data

    def get_hierarchies(self):
        return self.hierarchies