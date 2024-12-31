import numpy as np
import pandas as pd
from anjana.anonymity.utils import generate_intervals

# Bu sınıf, veri anonimleştirme süreçlerinde
# quasi-identifier (yarı-tanımlayıcı) sütunları için 
# genelleme seviyelerini (hierarchies) yönetmek amacıyla tasarlanmıştır. 


# Hiyerarşilerimi yöneteceğim ortak bir sınıftır. Burada genel metodları tanımlıyoruz.
class Hierarchy:
    def __init__(self,qi_name : str):
        
        # Her QI için bir hiyerarşi nesnesi oluşturuyoruz.
        self.qi_name = qi_name

        # Hiyerarşi seviyelerim
        self.levels = {}
    
    def add_level(self,level : int,values):

        # Hiyerarşimiz ile ilgili seviyeleri (level) buraya yazıyoruz.

        self.levels[level] = values

    def get_values(self,level :int):

        # İlgili seviyede dönüştürülen dizi döndürülecek.

        if level not in self.levels:
            raise ValueError(f"Hiyerarşi '{self.qi_name}' için level : {level} tanımlı değil.")
        return self.levels[level]




        
        