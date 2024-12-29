from AnonymizationPipeline import AnonymizationPipeline
from DataProcessor import DataProcessor
from OptimizationEngine import OptimizationEngine
from DataLossAnalyzer import DataLossAnalyzer
from AnonymityAnalyzer import AnonymityAnalyzer
from VisualizationEngine import VisualizationEngine
import time

def main():
    start = time.time()    
    data_path = "examples/data/adult_100.csv"
    hierarchy_folder = "examples/hierarchies"
    
    # Identifiers, Quasi-Identifiers ve Sensitive Attribute
    identifiers = ["race"]  # "race" sütunu identifiers olarak tanımlandı
    quasi_identifiers = ["age", "education", "marital-status", "occupation", "sex", "native-country"]
    sensitive_attribute = "salary-class"
    
    # k, l, t değerlerinin denenecek kombinasyonları
    k_values = [10, 20]
    l_values = [2, 2]
    t_values = [0.5, 0.4]

    print("Anonimleştirme işlemi hattı başlıyor...")

    try:
        # Pipeline oluştur
        pipeline = AnonymizationPipeline(data_path, hierarchy_folder)

        # Kombinasyonları denemek için bir döngü başlat
        for k in k_values:
            for l in l_values:
                for t in t_values:
                    print(f"\nAnonimlik seviyeleri: k={k}, l={l}, t={t}")
                    try:
                        # Anonimleştirme işlemi
                        anonymized_data = pipeline.run(
                            identifiers=identifiers,  # Identifiers burada belirtiliyor
                            quasi_identifiers=quasi_identifiers, 
                            sensitive_attribute=sensitive_attribute, 
                            k=k, 
                            l=l, 
                            t=t, 
                            suppression_level=30
                        )

                        # Anonimleştirilmiş veriyi kaydet
                        output_path = f"examples/data/anonymized_adult_k{k}_l{l}_t{t}_List.csv"
                        pipeline.save_anoymized_data(anonymized_data, output_path)
                        
                        # Anonimlik Analizi
                        print("\nAnonimlik Analizi Yapılıyor...")
                        analyzer = AnonymityAnalyzer(
                            pipeline.processor.get_data(),
                            anonymized_data,
                            quasi_identifiers,
                            sensitive_attribute
                        )

                        k_result = analyzer.calculate_k_anonymity()
                        l_result = analyzer.calculate_l_diversity()
                        t_result = analyzer.calculate_t_closeness()

                        print(f" - k-Anonymity : {k_result}")
                        print(f" - l-Diversity : {l_result}")
                        print(f" - t-Closeness : {t_result}")

                        # Bilgi Kaybı Analizi
                        print("\nBilgi Kaybı Analizi Yapılıyor...")
                        loss_analyzer = DataLossAnalyzer(
                            pipeline.processor.get_data(),
                            anonymized_data
                        )
                        suppression_rate = loss_analyzer.calculate_suppression_rate()
                        ncp = loss_analyzer.calculate_ncp()

                        print(f" - Baskılama Oranı : {suppression_rate * 100:.2f}%")
                        print(f" - NCP (Normalized Certainty Penalty) : {ncp:.4f}")

                    except Exception as e:
                        print(f"Anonimlik ve bilgi kaybı analizi sırasında hata oluştu: {e}")
                        continue

    except Exception as e:
        print(f"Anonimleştirme işlemi sırasında bir hata oluştu: {e}")
        return

    # Optimizasyon
    print("\n Optimizasyon başlatılıyor...")
    try:
        optimizer = OptimizationEngine(pipeline.processor)
        best_result, all_results = optimizer.optimize(
            quasi_identifiers=quasi_identifiers,
            sensitive_attribute=sensitive_attribute,
            hierarchies=pipeline.get_hierarchies(),
            k_values=k_values,
            l_values=l_values,
            t_values=t_values
        )
        print("\nEn İyi Optimizasyon Sonucu:")
        print(best_result)

        print("\nTüm Sonuçlar:")
        for result in all_results:
            print(result)

    except Exception as e:
        print(f"Optimizasyon sırasında hata oluştu: {e}")
        return
    
    # Optimizasyon sonuçlarını alıyoruz. (OptimizationEngine'den gelen sonuçlar)
    best_result,all_results = optimizer.optimize(
        quasi_identifiers = quasi_identifiers,
        sensitive_attribute = sensitive_attribute,
        hierarchies = pipeline.processor.get_hierarchies(),
        k_values=k_values,
        l_values=l_values,
        t_values=t_values
    )

    # VisualizationEngine kullanarak sonuçları görselleştir.
    visualizer = VisualizationEngine(all_results)

    # Fayda-Risk analizi grafiği
    visualizer.plot_fayda_risk()

    # Fayda metrikleri grafiği (k,l,t karşılaştırması)
    visualizer.plot_fayda_metrikleri()
    
    end = time.time()
    print("\nTüm işlemler tamamlandı, sonuçlarınızı kontrol ediniz.")
    print(f"\nToplam geçen süre: {end - start} saniye")

if __name__ == "__main__":
    main()
