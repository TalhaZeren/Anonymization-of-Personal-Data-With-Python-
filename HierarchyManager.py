from Hierarchy import Hierarchy

class HierarchyManager:

    
    def __init__(self):
        self.hierarchies = {}   # {"age" : AgeHierarchy(...), "sex": SexHierarchy(...), ....}

    def add_hierarchy(self,qi_name,hierarchy_obj :Hierarchy):

        self.hierarchies[qi_name] = hierarchy_obj

    def get_hierarchy_levels(self, qi_name: str) -> dict:


        # Anjana kütüphanesinin beklediği dictionary => {level: np.array, ...} döndür.

        if qi_name not in self.hierarchies:
            raise ValueError(f"{qi_name} için tanımlı bir hiyerarşi bulunamadı.")
        return self.hierarchies[qi_name].levels # Dictionary (level => array)
    
