from DataProcessor import DataProcessor
from Anonymizer import Anonymizer

class AnonymizationPipeline:
    def __init__(self, data_path, hierarchy_folder):
        """
        AnonymizationPipeline sınıfı, veri işleme ve anonimleştirme işlemlerini yürütür.
        """
        self.processor = DataProcessor(data_path, hierarchy_folder)

    def run(self, identifiers, quasi_identifiers, sensitive_attribute, k, l, t, suppression_level):
        """
        Belirtilen parametrelerle anonimleştirme işlemini çalıştırır.
        """
        # Veri sütunlarını kontrol et ve hiyerarşileri yükle
        self.processor.clean_columns(quasi_identifiers + identifiers + [sensitive_attribute])
        self.processor.load_hierarchies(quasi_identifiers)

        # Anonimleştirme işlemi
        anonymizer = Anonymizer(self.processor.get_data(), self.processor.get_hierarchies())
        data_k = anonymizer.apply_k_anonymity(identifiers, quasi_identifiers, k, suppression_level)
        data_l = anonymizer.apply_l_diversity(identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level)
        data_t = anonymizer.apply_t_closeness(identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level)

        return data_t

    def save_anoymized_data(self, data, output_path):
        """
        Anonimleştirilmiş veriyi bir dosyaya kaydeder.
        """
        try:
            data.to_csv(output_path, index=False)
            print(f"Anonimleştirilmiş veri {output_path} 'e kaydedildi.")
        except Exception as e:
            raise IOError("Anonimleştirilmiş veriyi kaydederken hata meydana geldi.") from e

    def get_hierarchies(self):
        """
        Hiyerarşileri döndürür.
        """
        return self.processor.get_hierarchies()
