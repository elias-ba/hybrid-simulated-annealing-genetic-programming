from conf import *
from genetic import evolve, crossover, mutation
from simulated_annealing import px_simulated_annealing, py_simulated_annealing

def simulation():
    results = []
    for PD in PDs:
        print(f"Optimisation pour le PD: {PD}")
        population = [
            [random.randint(MIN_PUISSANCE_BATTERIE, MAX_PUISSANCE_BATTERIE),
            random.randint(MIN_PUISSANCE_HYDROGENE, MAX_PUISSANCE_HYDROGENE)] 
            for _ in range(SIZE_POPULATION)
        ]
        if len(solutions := evolve(population, crossover, mutation, PD)) > 0:
            best = solutions[0]
            result_px = px_simulated_annealing(best[0], PD, 10)[0]
            result_py = py_simulated_annealing(best[1], PD, 10)[0]
            results.append(([result_px, result_py], PD, random.uniform(0.1, 0.5)))
    return results