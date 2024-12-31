import numpy as np
import pandas as pd
from Hierarchy import Hierarchy

class WorkclassHierarchy(Hierarchy):
    def __init__(self, data : pd.DataFrame):
        
        super().__init__("workclass")

        # Seviye 0 --> Orijinal değerler 

        self.add_level(0, data["workclass"].values)

        # Seviye 1 --> İlk Genelleştirme 
        workclass_generalization = {
            "Private": "Non-Government",
            "Self-emp-not-inc": "Non-Government",
            "Self-emp-inc": "Non-Government",
            "Federal-gov": "Government",
            "Local-gov": "Government",
            "State-gov": "Government",
            "Without-pay": "Unemployed",
            "Never-worked": "Unemployed",
            "?": "Unknown"
        } 

        self.add_level(
            1,
            pd.Series(data["workclass"].values).map(workclass_generalization).fillna("Unknown").values
        )
        
        # Seviye 2 --> Bastırma (Suppression)
        self.add_level(
            2,
            np.array(["*"] * len(data["workclass"].values))
        )