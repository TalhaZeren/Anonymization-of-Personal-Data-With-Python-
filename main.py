from DataProcessor import DataProcessor
from Anonymizer import Anonymizer
from PSOEngine import PSOEngine
from DataLossAnalyzer import DataLossAnalyzer
from AnonymityAnalyzer import AnonymityAnalyzer
from VisualizationEngine import VisualizationEngine
import time

def main():
    start = time.time()
    data_path = "examples/data/adult_100.csv"
    hierarchy_folder = "examples/hierarchies"

    quasi_identifiers = ["age", "education", "marital-status", "occupation", "sex", "native-country"]
    sensitive_attribute = "salary"

    print("Lütfen k, l, t aralıklarını belirtin:")
    k_bounds = (int(input("k için minimum değer: ")), int(input("k için maksimum değer: ")))
    l_bounds = (int(input("l için minimum değer: ")), int(input("l için maksimum değer: ")))
    t_bounds = (float(input("t için minimum değer: ")), float(input("t için maksimum değer: ")))

    # Veri işlemleri
    processor = DataProcessor(data_path, hierarchy_folder)
    processor.clean_columns(quasi_identifiers + [sensitive_attribute])
    processor.load_hierarchies(quasi_identifiers)

    # PSO için ağırlıklar
    weights = {
        "k": 0.3,
        "l": 0.2,
        "t": -0.2,
        "ncp": -0.2,
        "suppression_rate": -0.1
    }

    # PSO optimizasyon motorunu başlat
    pso_engine = PSOEngine(
        data_processor=processor,
        quasi_identifiers=quasi_identifiers,
        sensitive_attribute=sensitive_attribute,
        hierarchies=processor.get_hierarchies(),
        weights=weights
    )

    print("\nPSO ile optimizasyon başlıyor...")
    best_cost, best_position = pso_engine.optimize(k_bounds, l_bounds, t_bounds)

    print("\nEn İyi Skor:", best_cost)
    print("En İyi Parametreler (k, l, t):", best_position)

    # PSO'dan gelen parametreleri işleme
    k, l, t = int(best_position[0]), int(best_position[1]), best_position[2]

    # Anonimleştirme işlemi
    anonymizer = Anonymizer(processor.get_data(), processor.get_hierarchies())
    anonymized_data = anonymizer.apply_k_anonymity([], quasi_identifiers, k, 50)
    anonymized_data = anonymizer.apply_l_diversity([], quasi_identifiers, sensitive_attribute, k, l, 50)
    anonymized_data = anonymizer.apply_t_closeness([], quasi_identifiers, sensitive_attribute, k, t, 50)

    # Anonimleştirilmiş veriyi kaydet
    output_path = f"examples/data/anonymized_adult_k{k}_l{l}_t{t}_Best.csv"
    anonymized_data.to_csv(output_path, index=False)
    print(f"\nAnonimleştirilmiş veri {output_path} dosyasına kaydedildi.")

    # Anonimlik ve bilgi kaybı analizleri
    analyzer = AnonymityAnalyzer(processor.get_data(), anonymized_data, quasi_identifiers, sensitive_attribute)
    print("\nAnonimlik Analizi Sonuçları:")
    print(f" - k-Anonymity: {analyzer.calculate_k_anonymity()}")
    print(f" - l-Diversity: {analyzer.calculate_l_diversity()}")
    print(f" - t-Closeness: {analyzer.calculate_t_closeness()}")

    end = time.time()
    print(f"\nToplam geçen süre: {end - start:.2f} saniye")


if __name__ == "__main__":
    main()
