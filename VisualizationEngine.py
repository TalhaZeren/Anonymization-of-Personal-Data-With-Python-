from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class VisualizationEngine:
    def __init__(self,result):
        self.result = result
        # Optimize edilmiş anonimleştirme sonuçlarını listelememiz gerekiyor.
        # Her bir sonuç bir sözlük içermeli.

    
    def plot_fayda_risk(self,canvas):
        # Sonuçları DataFrame'e dönüştürür.
        df = pd.DataFrame(self.result)

        # Fayda-risk grafiği (Suppression ve NCP'ye göre yapıldı.)
        # Matplotlib figür ve eksen oluşturma 
        
        best_result = df.loc[df["score"].idxmax()]

        ax = canvas.figure.add_subplot(111)
        ax.clear()  # Önceki grafiği temizle

        ax.plot(
            df["suppression_rate"],
            df["ncp"],
            linestyle = "-", # Çizgiler ile bağlanması
            color = "gray",
            alpha = 0.5,
            label = "Durumlar (Line Chart)"
        )

        ax.scatter(
            df["suppression_rate"],
            df["ncp"],
            color="blue",
            alpha=0.7,
            label = "Diğer Durumlar"
        )   

        # En iyi sonucu işaretle

        ax.scatter(
            best_result["suppression_rate"],
            best_result["ncp"],
            color="red",
            s=100,
            label="En İyi Sonuç",
            edgecolors="black",
        )

        # Eksen ve Boşluklar
        ax.set_xlabel("Baskılama Oranı (Suppression Rate)")
        ax.set_ylabel("Normalized Certainty Penalty (NCP)")
        ax.set_title("Fayda-Risk Analizi")
        ax.legend()
        ax.grid(True)
        
        canvas.draw()


    def plot_fayda_metrikleri(self,canvas):

        # Fayda metriklerini (k,l,t gibi) bar plot olarak gösterir.

        df = pd.DataFrame(self.result) # Sonuçları DataFrame'e dönüştür.

        # K,L ve T için ayrı bar plot.
        
        melted_df = df.melt(
            id_vars=["score"],
            value_vars=["k","l","t"],
            var_name="Metric",
            value_name="Value",
        )

       # Matplotlib figür ve eksen oluşturma
        ax = canvas.figure.add_subplot(111)
        ax.clear()  # Önceki grafiği temizle


        sns.barplot(
            data=melted_df,
            x="Metric",
            y="Value",
            hue="score",
            ax=ax,
            palette="viridis"
            )
        
        # Eksenler, başlık ve grid
        ax.set_title("Anonimlik Metrikleri Karşılaştırması (k, l, t)")
        ax.set_ylabel("Değer")
        ax.set_xlabel("Metrik")
        ax.legend(title="Skor")
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        canvas.draw()

    def plot_pso_results(self,canvas,pso_results):
        # PSO sonuçları burada görselleştiriliyor.
        ax = canvas.figure.add_subplot(111)
        ax.clear()

        # PSO sonuçlarını grafik üzerinde göster.
        ax.bar(["k","l","t"], [pso_results["k"], pso_results["l"], pso_results["t"]], color = "blue")
        ax.set_title("PSO Optimizasyon Sonuçları")
        ax.set_ylabel("Değer")
        ax.set_xlabel("Parametreler")
        ax.grid(axis="y", linestyle = "--",alpha=0.7)

        canvas.draw()

        



