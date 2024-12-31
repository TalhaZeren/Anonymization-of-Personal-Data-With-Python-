import pandas as pd
from HierarchyManager import HierarchyManager
from Hierarchies import AgeHierarchy
from Hierarchies import EducationHierarchy
from Hierarchies import MaritalStatusHierarchy
from Hierarchies import NativeCountryHierarchy
from Hierarchies import OccupationHierarchy
from Hierarchies import RaceHierarchy
from Hierarchies import SexHierarchy
from Hierarchies import WorkclassHierarchy
from Hierarchies import SalaryHierarchy
class DataProcessor:

    def __init__(self, data_path: str):
        self.data = pd.read_csv(data_path)
        self.hierarchies = {} # Buraya dictionary olarak set ediyoruz.

    def clean_columns(self):
        """
        Gerekli sütun temizleme işlemlerini yapar.
        Örneğin, eksik değerleri doldurmak veya belirli sütunları silmek.
        """
        # Örnek: Eksik değerleri "Unknown" ile doldurmak
        self.data.fillna("Unknown", inplace=True)

    def load_hierarchies(self, quasi_identifiers, manager : HierarchyManager):
        
        for qi in quasi_identifiers:
            if qi == "age":
                age_hier = AgeHierarchy(self.data)
                manager.add_hierarchy("age", age_hier)
            elif qi == "education":
                education_hier = EducationHierarchy(self.data)
                manager.add_hierarchy("education", education_hier)
            elif qi == "marital-status":
                marital_hier = MaritalStatusHierarchy(self.data)
                manager.add_hierarchy("marital-status", marital_hier)
            elif qi == "native-country":
                native_country_hier = NativeCountryHierarchy(self.data)
                manager.add_hierarchy("native-country", native_country_hier)
            elif qi == "occupation":
                occupation_hier = OccupationHierarchy(self.data)
                manager.add_hierarchy("occupation", occupation_hier)
            elif qi == "race":
                race_hier = RaceHierarchy(self.data)
                manager.add_hierarchy("race", race_hier)
            elif qi == "sex":
                sex_hier = SexHierarchy(self.data)
                manager.add_hierarchy("sex", sex_hier)
            elif qi == "workclass":
                workclass_hier = WorkclassHierarchy(self.data)
                manager.add_hierarchy("workclass", workclass_hier)
            elif qi == "salary":
                salary_hier = SalaryHierarchy(self.data)
                manager.add_hierarchy("salary", salary_hier)
            else:
                raise ValueError(f"Qi '{qi}' için hiyerarşi sınıfı tanımlanmadı.")
        self.hierarchies = manager.hierarchies
        print("Hiyerarşiler başarıyla yüklendi.")

        
            # Eski kod. Deneme amaçlı bırakıldı.
    """
        for qi in quasi_identifiers:
            hierarchy_file = f"{self.hierarchy_folder}/{qi}.csv"
            print(hierarchy_file)
            try:
                self.hierarchies[qi] = dict(pd.read_csv(hierarchy_file, header=None))

            except FileNotFoundError:
                raise FileNotFoundError(f"{qi} için hiyerarşi dosyası bulunamadı: {hierarchy_file}")
            except Exception as e:
                raise ValueError(f"Hiyerarşi yüklenirken hata oluştu: {qi}, {e}")
    """
    def preprocess_numeric_columns(self, numeric_columns):
        for col in numeric_columns:
            if col in self.data.columns:
                self.data[col] = pd.to_numeric(self.data[col], errors="coerce")
    
    def get_data(self):
        return self.data   # Orjinal veriyi döndürüyor.

    def get_hierarchies(self):
        return self.hierarchies
