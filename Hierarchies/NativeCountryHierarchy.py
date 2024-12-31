import numpy as np
import pandas as pd
from Hierarchy import Hierarchy


class NativeCountryHierarchy(Hierarchy):
    
    def __init__(self, data: pd.DataFrame):
    
        super().__init__("native-country")


        # Seviye 0 --> Orijinal Değerler

        self.add_level(0,data["native-country"].values)

        # Seviye 1 --> İlk Genelleştirme (Kıta bazında yapılıyor...)

        native_country_generalization = {
            "United-States": "North America",
            "Cambodia": "Asia",
            "England": "Europe",
            "Puerto-Rico": "North America",
            "Canada": "North America",
            "Germany": "Europe",
            "Outlying-US(Guam-USVI-etc)": "North America",
            "India": "Asia",
            "Japan": "Asia",
            "Greece": "Europe",
            "South": "Africa",
            "China": "Asia",
            "Cuba": "North America",
            "Iran": "Asia",
            "Honduras": "North America",
            "Philippines": "Asia",
            "Italy": "Europe",
            "Poland": "Europe",
            "Jamaica": "North America",
            "Vietnam": "Asia",
            "Mexico": "North America",
            "Portugal": "Europe",
            "Ireland": "Europe",
            "France": "Europe",
            "Dominican-Republic": "North America",
            "Laos": "Asia",
            "Ecuador": "South America",
            "Taiwan": "Asia",
            "Haiti": "North America",
            "Columbia": "South America",
            "Hungary": "Europe",
            "Guatemala": "North America",
            "Nicaragua": "South America",
            "Scotland": "Europe",
            "Thailand": "Asia",
            "Yugoslavia": "Europe",
            "El-Salvador": "North America",
            "Trinadad&Tobago": "South America",
            "Peru": "South America",
            "Hong": "Asia",
            "Türkiye": "Asia",
            "Holand-Netherlands": "Europe",
            "?": "Unknown"
        }

        self.add_level(
            1,
            pd.Series(data["native-country"].values).map(native_country_generalization).fillna("Unknown").values
        )

        self.add_level(
            2,
            np.array(["*"] * len(data["native-country"].values))
        )