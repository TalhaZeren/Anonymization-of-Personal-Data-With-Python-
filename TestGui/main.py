import pandas as pd
from AnonymizationApp import AnonymizationApp
from OptimizationEngine import OptimizationEngine
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem)


# Veri seti oluşturma
data = pd.DataFrame({
    "age": [25, 35, 45, 55, 65],
    "education": ["Bachelor", "Master", "PhD", "Bachelor", "Master"],
    "marital-status": ["Married", "Single", "Divorced", "Married", "Single"],
    "occupation": ["Engineer", "Doctor", "Lawyer", "Engineer", "Teacher"],
    "sex": ["Male", "Female", "Male", "Female", "Male"],
    "native-country": ["US", "UK", "US", "India", "China"],
    "salary-class": ["<=50K", ">50K", "<=50K", ">50K", "<=50K"]
})

# Hiyerarşiler
hierarchies = {
    "age": {25: "20-30", 35: "30-40", 45: "40-50", 55: "50-60", 65: "60-70"},
    "education": {"Bachelor": "Undergrad", "Master": "Postgrad", "PhD": "Postgrad"},
    "marital-status": {"Married": "M", "Single": "S", "Divorced": "D"},
    "occupation": {"Engineer": "Tech", "Doctor": "Health", "Lawyer": "Legal", "Teacher": "Education"},
    "sex": {"Male": "M", "Female": "F"},
    "native-country": {"US": "North America", "UK": "Europe", "India": "Asia", "China": "Asia"}
}

# Optimizasyon sınıfını başlat
engine = OptimizationEngine(
    data,
    hierarchies,
    quasi_identifiers=["age", "education", "marital-status", "occupation", "sex", "native-country"],
    sensitive_attribute="salary-class"
)

# PSO ile optimize et
best_cost, best_params = engine.optimize(
    k_bounds=(3, 50),
    l_bounds=(2, 10),
    t_bounds=(0.01, 1.0)
)
print(f"En iyi skor: {best_cost}, En iyi parametreler: {best_params}")