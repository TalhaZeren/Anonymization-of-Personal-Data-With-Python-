import numpy as np
import pandas as pd
from Hierarchy import Hierarchy


class MaritalStatusHierarchy(Hierarchy):

    def __init__(self, data : pd.DataFrame):

        # DataFrame marital-status sütununu içermeli. 

        super().__init__("marital-status")

        # Seviye 0 --> Orijinal değerler
        self.add_level(0, data["marital-status"].values)


        # Seviye 1 --> İlk Genelleştirme 
        marital_status_generalization = {
            "Married-civ-spouse": "Spouse present",
            "Divorced": "Spouse not present",
            "Never-married": "Spouse not present",
            "Separated": "Spouse not present",
            "Widowed": "Spouse not present",
            "Married-spouse-absent": "Spouse not present",
            "Married-AF-spouse": "Spouse present",
            "?": "Unknown"
        }

        self.add_level(
            1,
            pd.Series(data["marital-status"].values).map(marital_status_generalization).fillna("Unknown").values
        )

        # Seviye 2 --> Bastırma (Suppression)
        self.add_level(
            2,
            np.array(["*"] * len(data["marital-status"].values))
        )
        