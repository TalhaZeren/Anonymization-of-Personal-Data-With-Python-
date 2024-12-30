import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

class VisualizationEngine:
    def __init__(self,result):
        self.result = result
        # Optimize edilmiş anonimleştirme sonuçlarını listelememiz gerekiyor.
        # Her bir sonuç bir sözlük içermeli.

    
    def plot_fayda_risk(self):

        # Sonuçları DataFrame'e dönüştürür.
        df = pd.DataFrame(self.result)

        # Fayda-risk grafiği (Suppression ve NCP'ye göre yapıldı.)
        plt.scatter(
            df["suppression_rate"],
            df["ncp"],
            color="black",
            alpha=0.5,
            label = "Diğer Durumlar"
        )   

        # En iyi sonucu işaretle
        best_result = df.loc[df["score"].idxmax()]
        plt.scatter(
            best_result["suppression_rate"],
            best_result["ncp"],
            color="red",
            s=300,
            label="En İyi Sonuç",
            edgecolors="black",
        )

        # Eksen ve Boşluklar

        plt.xlabel("Baskılama Oranı (Suppression Rate)")
        plt.ylabel("Normalized Certainty Penalty (NCP)")
        plt.title("Fayda-Risk Analizi")
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_fayda_metrikleri(self):

        # Fayda metriklerini (k,l,t gibi) bar plot olarak gösterir.

        df = pd.DataFrame(self.result) # Sonuçları DataFrame'e dönüştür.

        # K,L ve T için ayrı bar plot.
        plt.figure(figsize=(12,6))
        melted_df = df.melt(
            id_vars=["score"],
            value_vars=["k","l","t"],
            var_name="Metric",
            value_name="Value"
        )

        sns.barplot(data=melted_df,x="Metric",y="Value",hue="score",palette="viridis")
        plt.title("Anonimlik Metrikleri Karşılaştırması (k,l,t)")
        plt.ylabel("Değer")
        plt.xlabel("Metrik")
        plt.legend(title="Skor")
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

        



