import numpy as np
from Hierarchy import Hierarchy
import pandas as pd

class RaceHierarchy(Hierarchy):
    def __init__(self, data: pd.DataFrame ):
      
        # DataFrame, en azından 'race' sütununu içermeli.
        super().__init__("race")
        
        # Seviye 0 --> Orijinal Değerler
        self.add_level(0,data["race"].values)

        # Seviye 1 : Bastırma (Suppression)
        self.add_level(
            1,
            np.array(["*"] * len(data["race"].values))
        )
