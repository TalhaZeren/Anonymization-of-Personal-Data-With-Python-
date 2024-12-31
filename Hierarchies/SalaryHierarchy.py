import numpy as np
from Hierarchy import Hierarchy
import pandas as pd

class SalaryHierarchy(Hierarchy):
    def __init__(self,data: pd.DataFrame):

        super().__init__("salary")

        # Seviye 0 --> Orijnal değerler
        self.add_level(0,data["salary"].values)


        # Seviye 1 --> Bastırma (Suppression) --> Hassas veri olabilir.
        self.add_level(
            1,
            np.array(["*"] * len(data["salary"].values))
        )
        
        