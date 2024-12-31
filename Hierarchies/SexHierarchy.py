import numpy as np
from Hierarchy import Hierarchy
import pandas as pd

class SexHierarchy(Hierarchy):
    def __init__(self, data:pd.DataFrame):
        super().__init__("sex")

        # Seviye 0 --> Orijinal değerler

        self.add_level(0, data["sex"].values)

        # Seviye 1 : Bastırma (Suppression)
        self.add_level(
            1,
            np.array(["*"] * len(data["sex"].values))
        )

        

        