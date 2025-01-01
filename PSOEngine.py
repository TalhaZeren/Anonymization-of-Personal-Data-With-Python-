import numpy as np
import pyswarms as ps
from Anonymizer import Anonymizer
from AnonymityAnalyzer import AnonymityAnalyzer
from DataLossAnalyzer import DataLossAnalyzer

class PSOEngine:
    def __init__(self, data_processor, quasi_identifiers, sensitive_attribute, hierarchies, weights):
        self.data_processor = data_processor
        self.quasi_identifiers = quasi_identifiers
        self.sensitive_attribute = sensitive_attribute
        self.hierarchies = hierarchies
        self.weights = weights

    def fitness_function(self, params):
        k, l, t = params[:, 0], params[:, 1], params[:, 2]
        scores = []

        for i in range(len(k)):
            try:
                anonymizer = Anonymizer(self.data_processor.get_data(), self.hierarchies)
                data_anon = anonymizer.apply_k_anonymity([], self.quasi_identifiers, int(k[i]), 50)
                data_anon = anonymizer.apply_l_diversity([], self.quasi_identifiers, self.sensitive_attribute, int(k[i]), int(l[i]), 50)
                data_anon = anonymizer.apply_t_closeness([], self.quasi_identifiers, self.sensitive_attribute, int(k[i]), t[i], 50)

                analyzer = AnonymityAnalyzer(self.data_processor.get_data(), data_anon, self.quasi_identifiers, self.sensitive_attribute)
                k_result = analyzer.calculate_k_anonymity()
                l_result = analyzer.calculate_l_diversity()
                t_result = analyzer.calculate_t_closeness()

                loss_analyzer = DataLossAnalyzer(self.data_processor.get_data(), data_anon)
                suppression_rate = loss_analyzer.calculate_suppression_rate()
                ncp = loss_analyzer.calculate_ncp()

                score = (
                    self.weights["k"] * k_result +
                    self.weights["l"] * l_result -
                    self.weights["t"] * t_result -
                    self.weights["ncp"] * ncp -
                    self.weights["suppression_rate"] * suppression_rate
                )
                scores.append(score)
            except Exception as e:
                scores.append(-np.inf)

        return np.array(scores)

    def optimize(self, k_bounds, l_bounds, t_bounds, n_particles=20, iters=50):
        options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
        bounds = (np.array([k_bounds[0], l_bounds[0], t_bounds[0]]), np.array([k_bounds[1], l_bounds[1], t_bounds[1]]))

        optimizer = ps.single.GlobalBestPSO(n_particles=n_particles, dimensions=3, options=options, bounds=bounds)
        best_cost, best_position = optimizer.optimize(self.fitness_function, iters=iters)

        return best_cost, best_position