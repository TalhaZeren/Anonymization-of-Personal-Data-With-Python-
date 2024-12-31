from DataProcessor import DataProcessor
from HierarchyManager import HierarchyManager
from Anonymizer import Anonymizer  # Anonymizer sınıfınızı doğru şekilde içe aktarın
import pandas as pd

class AnonymizationPipeline:
    def __init__(self, data_path :str):
        self.processor = DataProcessor(data_path)

    def run(self, identifiers, quasi_identifiers, sensitive_attribute, k, l, t, suppression_level):

        """
        Anonimleştirme sürecini yürütür.
        :param identifiers: Identifiers listesi.
        :param quasi_identifiers: Quasi-Identifiers listesi.
        :param sensitive_attribute: Duyarlı öznitelik.
        :param k: k-anonimlik seviyesi.
        :param l: l-çeşitlilik seviyesi.
        :param t: t-yakınlık seviyesi.
        :param suppression_level: Baskılama seviyesi (örneğin, %50).
        :return: Anonimleştirilmiş veri seti.
        """

        # Sütunları temizleme işlemi
        self.processor.clean_columns()
       
        self.processor.preprocess_numeric_columns(["age"])
         # Hiyerarşileri yükleme
        manager = HierarchyManager()
        self.processor.load_hierarchies(quasi_identifiers,manager)

        # Anonimleştirme adımları
        anonymizer = Anonymizer(self.processor.get_data(), self.processor.get_hierarchies())
        anoymized_data = anonymizer.apply_k_anonymity(identifiers, quasi_identifiers, k, suppression_level)
        anoymized_data = anonymizer.apply_l_diversity(identifiers, quasi_identifiers, sensitive_attribute, k, l, suppression_level)
        anoymized_data = anonymizer.apply_t_closeness(identifiers, quasi_identifiers, sensitive_attribute, k, t, suppression_level)
        return anoymized_data

    def save_anonymized_data(self, data, output_path):
        try:
            data.to_csv(output_path, index=False)
            print(f"Anonimleştirilmiş veri {output_path} 'e kaydedildi.")
        except Exception as e:
            raise IOError("Anonimleştirilmiş veriyi kaydederken hata meydana geldi.") from e

    def get_hierarchies(self):
       
        return self.processor.get_hierarchies()
