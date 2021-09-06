from numpy import random, array
from conf import *
from simulated_annealing import *

def fitness(chromosome, pd):
    x, y = chromosome
    dpd = (1 - (pd - (x + y))/70) * 100
    dxy = (y/60) * 100
    return dpd, dxy

def crossover(chromosome_a, chromosome_b, pd):
    f1, f2 = fitness(chromosome_a, pd), fitness(chromosome_b, pd)
    px = chromosome_a[0] if abs(100 - f1[0]) < abs(100 - f2[0]) else chromosome_b[0]
    py = chromosome_a[1] if f1[1] < f2[1] else chromosome_b[1]
    return [px, py]

def alive(chromosome, pd):
    f = fitness(chromosome, pd)
    return f[0] >= 100 and 0 <= f[1] < 50  

def mutation(chromosome, coeff_mutation_a, coeff_mutation_b, proba_mutation):
    if 25 < proba_mutation < 75 and chromosome[1] + coeff_mutation_b > 0:
        chromosome[0] += coeff_mutation_a 
        chromosome[1] += coeff_mutation_b
    return chromosome

def get_mutation_params():
    return random.uniform(-1, 1), random.uniform(-1, 1), random.randint(0, 100)

def get_pairs(population):
    return [
        [chromosome_a, chromosome_b] 
        for chromosome_a, chromosome_b in zip(
            population[:len(population)//2],
            population[len(population)//2:]
        )
    ]

def select_best(population, k=1):
    sorted_population = sorted(population, key=lambda chromosome: chromosome[1])
    return sorted_population[:k]

def evolve(population, crossover, mutation, PD, k_best=1):
    for generation_number in range(N_GENERATIONS):
        print(f"Generation numero {generation_number + 1}...")
        population = [chromosome for chromosome in population if alive(chromosome, PD)]
        population.extend(
            crossover(chromosome_a, chromosome_b, PD) 
            for chromosome_a, chromosome_b in get_pairs(population)
        )
        population = [mutation(chromosome, *get_mutation_params()) 
            for chromosome in population
        ]
    return select_best(population, k_best)
