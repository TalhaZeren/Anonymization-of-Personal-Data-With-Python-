import numpy as np
import pandas as pd
from anjana.anonymity.utils import generate_intervals
from Hierarchy import Hierarchy

class AgeHierarchy(Hierarchy):
    def __init__(self, data: pd.DataFrame):

        # data : DataFrame, age sütununu içermeli. 
        
        super().__init__("age")  # Burada üst sınıfa QI adını gönderiyoruz.

        # 0. Seviye --> Orijinal değerlerdir.

        # Burada istediğimiz kadar hiyearşi tanımlayabiliriz.Fakat veri setinin sınırlarına dikkat etmeliyiz.

        self.add_level(0, data["age"].values)

        self.add_level(
            1,
            generate_intervals(data["age"].values, inf = 0, sup=80, step=5)
        )

        self.add_level(
            2,
            generate_intervals(data["age"].values, inf=0, sup=80, step=10)
        )
        
        self.add_level(
            3,
            generate_intervals(data["age"].values, inf=0,sup=80,step=20)
        )
        self.add_level(
            4,
            generate_intervals(data["age"].values, inf=0,sup=80,step=40)
        )
        self.add_level(
            5,
            generate_intervals(data["age"].values, inf=0,sup=80,step=80)
        )

        suppression = np.array(["*"] * len(data))
        self.add_level(6,suppression)
         
    