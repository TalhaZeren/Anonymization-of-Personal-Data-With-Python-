from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QSplitter,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QMainWindow,
    QFileDialog,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class UI(QMainWindow):
    def __init__(self, callback):
        super().__init__()

        self.callback = callback # Main sınıfına veri göndermek için bir referans.
        self.setWindowTitle("Anonimleştirme ve Optimizasyon") # Pencere başlığımız
        self.setGeometry(300,300,1400,800) # Daha büyük pencere boyutu 

        # Ana widget ve layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        main_layout = QHBoxLayout(self.central_widget)  # Yatay bir layout oluşturduk

        #Bölümleri ayırmak için QSplitter kullanıyoruz.
        splitter = QSplitter(self.central_widget)

        #Grafik Bölümü 
        self.graph_widget = QWidget() #Grafiklerin gösterileceği alan
        graph_layout = QVBoxLayout(self.graph_widget)

        # Matplotlib canvas ekle
        self.figure_Optimum = Figure()  # Optimum grafiği için figür
        self.canvas_Optimum = FigureCanvas(self.figure_Optimum) # Optimum grafik için canvas
        graph_layout.addWidget(self.canvas_Optimum)

        self.figure_Metrics = Figure() # Metrik grafiği için figür
        self.canvas_Metrics = FigureCanvas(self.figure_Metrics) # Metrik grafiği için canvas
        graph_layout.addWidget(self.canvas_Metrics)

        self.figure_PSO = Figure() # PSO sonuçları için figür oluşturuluyor.
        self.canvas_PSO = FigureCanvas(self.figure_PSO)
        graph_layout.addWidget(self.canvas_PSO)

        splitter.addWidget(self.graph_widget)

        # Giriş Bölümü
        self.input_widget = QWidget() # Değer giriş alanları
        input_layout = QVBoxLayout(self.input_widget)

        # Giriş alanları ve etiketler

        # k-anonimlik metrik değeri
        self.input_k = QLineEdit()
        self.input_k.setPlaceholderText("k-Anonimlik değerini giriniz")
        # l-diversity metrik değeri
        self.input_l = QLineEdit()
        self.input_l.setPlaceholderText("l-Diversity değerini giriniz")
         # t-closeness metrik değeri
        self.input_t = QLineEdit()
        self.input_t.setPlaceholderText("t-Closeness değerini giriniz")
       
        self.submit_button = QPushButton("Gönder") # Değerleri göndermek için buton
        self.submit_button.clicked.connect(self.send_data) # Butona tıklama olayını bağla


        # Giriş alanlarını ve butonu layout'a ekle
        input_layout.addWidget(QLabel("Anonimlik Değerlerini Girin:"))
        input_layout.addWidget(self.input_k)
        input_layout.addWidget(self.input_l)
        input_layout.addWidget(self.input_t)
        # Onay butonu
        input_layout.addWidget(self.submit_button) 


        # PSO sonuçlarını göstermek için bir metin alanı
        self.pso_results_label = QLabel("PSO ile Optimizasyon Sonuçları\n")
        input_layout.addWidget(self.pso_results_label)

        splitter.addWidget(self.input_widget)

        #Splitter'ı ana layout'a ekle
        main_layout.addWidget(splitter)
    
    def send_data(self):
        #Kullanıcıdan alınan değerleri callback ile Main sınıfına gönderiyoruz.

        value_k = self.input_k.text().split(',')
        value_l = self.input_l.text().split(',')
        value_t = self.input_t.text().split(',')
        

        self.callback(value_k,value_l,value_t)

    def show_fayda_risk(self,visualizer):
        #Fayda-Risk analizi grafiğini göster.
        self.figure_Optimum.clear()
        visualizer.plot_fayda_risk(self.canvas_Optimum)

    def show_fayda_metrikleri(self,visualizer):
        #Fayda Metrikleri grafiğini göster.
        self.figure_Metrics.clear()
        visualizer.plot_fayda_metrikleri(self.canvas_Metrics)

    def show_pso_results(self, visualizer, pso_results):
        # PSO sonuçlarını görselleştir.
        self.figure_PSO.clear() # Önceki sonucu temizle.
        visualizer.plot_pso_results(self.canvas_PSO, pso_results)

        self.pso_results_label.setText(
            f"PSO Sonuçları:\n"
            f"En iyi k-anonimlik değeri: {pso_results['k']}\n"
            f"En iyi l-diversity değeri: {pso_results['l']}\n"
            f"En iyi t-closeness değeri: {pso_results['t']}\n"
            f"Skor: {pso_results['score']:.4f}"
        )



















        #######   Önceki işlemler #########





    #     self.input_k = QLineEdit()
    #     self.input_k.setPlaceholderText("k-Anonimlik değerini giriniz.") 
    #     self.input_l = QLineEdit()
    #     self.input_l.setPlaceholderText("l-Diverstiy değerini giriniz.") 
    #     self.input_t = QLineEdit()
    #     self.input_t.setPlaceholderText("t-Closeness değerini giriniz.")

    #     self.submit_button = QPushButton("Uygula") 

    #     # Spacer ekleyerek bileşenleri ortaıyoruz.
    #     spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    #     spacer_bottom = QSpacerItem(20,40,QSizePolicy.Minimum, QSizePolicy.Expanding)


    #     # Bileşenleri Layout'a eklediğim bölüm
    #     self.layout.addItem(spacer_top) # Üst Boşluk
    #     self.layout.addWidget(QLabel("Lütfen metrik değerlerini giriniz:"))
    #     self.layout.addWidget(self.input_k)  # Birinci girdi alanını ekle
    #     self.layout.addWidget(self.input_l)  # İkinci girdi alanını ekle
    #     self.layout.addWidget(self.input_t)  # Üçüncü girdi alanını ekle
    #     self.layout.addWidget(self.submit_button)  # Gönder butonunu ekle
    #     self.layout.addItem(spacer_bottom) # Alt Boşluk
    #     self.submit_button.clicked.connect(self.send_data)

    # def send_data(self):
    #     # Girdi alanlarından verileri alıyoruz.
    #     value_k = self.input_k.text().split(',')
    #     value_l = self.input_l.text().split(',')
    #     value_t = self.input_t.text().split(',')
        
    #     self.callback(value_k,value_l,value_t)
