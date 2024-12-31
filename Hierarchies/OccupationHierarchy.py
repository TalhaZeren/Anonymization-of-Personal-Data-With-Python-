import numpy as np
import pandas as pd
from Hierarchy import Hierarchy

class OccupationHierarchy(Hierarchy):
    def __init__(self, data: pd.DataFrame):
        super().__init__("occupation")


        # Seviye 0 --> Orijinal Değerler

        self.add_level(0, data["occupation"].values)

        # Seviye 1 --> İlk Genelleştirme 
        occupation_generalization= {
             "Tech-support": "Technical",
            "Craft-repair": "Technical",
            "Other-service": "Other",
            "Sales": "Nontechnical",
            "Exec-managerial": "Nontechnical",
            "Prof-specialty": "Technical",
            "Handlers-cleaners": "Nontechnical",
            "Machine-op-inspct": "Technical",
            "Adm-clerical": "Other",
            "Farming-fishing": "Other",
            "Transport-moving": "Other",
            "Priv-house-serv": "Other",
            "Protective-serv": "Other",
            "Armed-Forces": "Other",
            "?": "Unknown"
        }

        self.add_level(
            1,
            pd.Series(data["occupation"].values).map(occupation_generalization).fillna("Unknown").values
        )

        # Seviye 2 : Bastırma (Suppression)
        self.add_level(
            2,
            np.array(["*"] * len(data["occupation"].values))
        )

        
