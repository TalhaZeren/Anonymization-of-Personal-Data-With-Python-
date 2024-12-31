import numpy as np 
import pandas as pd
from anjana.anonymity.utils import generate_intervals
from Hierarchy import Hierarchy


class EducationHierarchy(Hierarchy):
    def __init__(self, data : pd.DataFrame):
        
        super().__init__("education")
        
        # Seviye 0 --> orijinal veriler
        self.add_level(0,data["education"].values)

        # Seviye 1 --> İlk genelleştirme 
        education_generalization = {
            "Bachelors": "Higher education",
            "Undergraduate": "Higher education",
            "Higher education": "Higher education",
            "Some-college": "Undergraduate",
            "11th": "Secondary education",
            "HS-grad": "Secondary education",
            "Prof-school": "Higher education",
            "Assoc-acdm": "Professional Education",
            "Assoc-voc": "Professional Education",
            "9th": "Secondary education",
            "7th-8th": "Secondary education",
            "12th": "Secondary education",
            "Masters": "Graduate",
            "1st-4th": "Primary education",
            "10th": "Secondary education",
            "Doctorate": "Graduate",
            "5th-6th": "Primary education",
            "Preschool": "Primary education",
            "?": "Unknown"  # Eğer '?' varsa 'Unknown' olarak genelleştirebilirsiniz
        }

        self.add_level(
            1,
            pd.Series(data["education"].values).map(education_generalization).fillna("Unknown").values
        )

        # Seviye 2 için --> Bastırma (Suppression)
        self.add_level(
            2,
            np.array(["*****"] * len(data["education"].values))
        )