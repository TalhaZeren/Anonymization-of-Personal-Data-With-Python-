# VisualizationEngine Class
class VisualizationEngine:
    def __init__(self, results):
        self.results = results
        self.df = pd.DataFrame(self.results)

    def plot_fayda_risk(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df["suppression_rate"], self.df["ncp"], color="black", alpha=0.5, label="Diğer Durumlar")
        best_result = self.df.loc[self.df["score"].idxmax()]
        plt.scatter(best_result["suppression_rate"], best_result["ncp"], color="red", s=300, label="En İyi Sonuç", edgecolors="black")
        plt.xlabel("Baskılama Oranı (Suppression Rate)")
        plt.ylabel("Normalized Certainty Penalty (NCP)")
        plt.title("Fayda-Risk Analizi")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.show()

    def plot_fayda_metrikleri(self):
        melted_df = self.df.melt(id_vars=["score"], value_vars=["k", "l", "t"], var_name="Metric", value_name="Value")
        sns.barplot(data=melted_df, x="Metric", y="Value", hue="score", palette="viridis")
        plt.title("Anonimlik Metrikleri Karşılaştırması (k, l, t)")
        plt.ylabel("Değer")
        plt.xlabel("Metrik")
        plt.legend(title="Skor", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.tight_layout()
        plt.show()

    def plot_score_distribution(self):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df["score"], kde=True, color="blue", bins=20)
        plt.title("Skor Dağılımı")
        plt.xlabel("Skor")
        plt.ylabel("Frekans")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.show()

    def plot_suppression_vs_score(self):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=self.df, x="suppression_rate", y="score", marker="o", color="green")
        plt.title("Baskılama Oranı vs Skor")
        plt.xlabel("Baskılama Oranı (Suppression Rate)")
        plt.ylabel("Skor")
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.show()
