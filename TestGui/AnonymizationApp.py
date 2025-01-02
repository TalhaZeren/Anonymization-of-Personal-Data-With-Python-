from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem
import matplotlib.pyplot as plt

class AnonymizationApp(QMainWindow):
    def __init__(self, optimization_engine):
        super().__init__()
        self.engine = optimization_engine

        self.setWindowTitle("Anonimleştirme ve Optimizasyon")
        self.setGeometry(100, 100, 800, 600)

        self.k_min_input = QLineEdit(self)
        self.k_max_input = QLineEdit(self)
        self.l_min_input = QLineEdit(self)
        self.l_max_input = QLineEdit(self)
        self.t_min_input = QLineEdit(self)
        self.t_max_input = QLineEdit(self)

        self.start_button = QPushButton("Optimizasyonu Başlat", self)
        self.start_button.clicked.connect(self.start_optimization)

        self.result_table = QTableWidget(self)
        self.result_table.setColumnCount(4)
        self.result_table.setHorizontalHeaderLabels(["K", "L", "T", "Skor"])

        layout = QVBoxLayout()
        layout.addWidget(QLabel("K Min:"))
        layout.addWidget(self.k_min_input)
        layout.addWidget(QLabel("K Max:"))
        layout.addWidget(self.k_max_input)

        layout.addWidget(QLabel("L Min:"))
        layout.addWidget(self.l_min_input)
        layout.addWidget(QLabel("L Max:"))
        layout.addWidget(self.l_max_input)

        layout.addWidget(QLabel("T Min:"))
        layout.addWidget(self.t_min_input)
        layout.addWidget(QLabel("T Max:"))
        layout.addWidget(self.t_max_input)

        layout.addWidget(self.start_button)
        layout.addWidget(self.result_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_optimization(self):
        k_min = int(self.k_min_input.text())
        k_max = int(self.k_max_input.text())
        l_min = int(self.l_min_input.text())
        l_max = int(self.l_max_input.text())
        t_min = float(self.t_min_input.text())
        t_max = float(self.t_max_input.text())

        best_cost, best_params = self.engine.optimize(
            k_bounds=(k_min, k_max),
            l_bounds=(l_min, l_max),
            t_bounds=(t_min, t_max)
        )

        self.result_table.setRowCount(1)
        self.result_table.setItem(0, 0, QTableWidgetItem(str(int(best_params[0]))))
        self.result_table.setItem(0, 1, QTableWidgetItem(str(int(best_params[1]))))
        self.result_table.setItem(0, 2, QTableWidgetItem(f"{best_params[2]:.2f}"))
        self.result_table.setItem(0, 3, QTableWidgetItem(f"{best_cost:.2f}"))

        self.show_results(best_cost, best_params)

    def show_results(self, best_cost, best_params):
        plt.figure(figsize=(10, 6))
        plt.scatter(best_params[0], best_cost, color="red", label="Optimum Sonuç", s=100)
        plt.title("Fayda-Risk Optimizasyon Sonuçları")
        plt.xlabel("K Değeri")
        plt.ylabel("Skor")
        plt.legend()
        plt.grid(True)
        plt.show()
