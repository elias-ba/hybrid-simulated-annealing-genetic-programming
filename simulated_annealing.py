from numpy.random import randint
from numpy import exp
from conf import *

def px_objective(px, pd):
    """Minimiser"""
    return pd - px

def py_objective(py, pd):
    """Maximiser"""
    return pd - py

def px_simulated_annealing(px, pd, temp, objective=px_objective):
	best_score = objective(px, pd)
	curr_px, curr_score = px, best_score
	for i in range(1000):
		candidate_px = curr_px + randint(
            MIN_PUISSANCE_BATTERIE, MAX_PUISSANCE_BATTERIE
        ) * 0.1
		candidate_score = objective(candidate_px, pd)

		if (candidate_score < best_score) and (MIN_PUISSANCE_BATTERIE < candidate_px < MAX_PUISSANCE_BATTERIE):
			px, best_score = candidate_px, candidate_score

		diff = candidate_score - curr_score

		t = temp / float(i + 1)

		sigmoid = 1 / (1 + exp(-diff / t))

		if sigmoid <= 0.5:
			curr_px, curr_score = candidate_px, candidate_score
    
	return [px, best_score]

def py_simulated_annealing(py, pd, temp, objective=py_objective):
    best_score = objective(py, pd)
    curr_py, curr_score = py, best_score
    for i in range(1000):
        candidate_py = curr_py + randint(
            MIN_PUISSANCE_HYDROGENE, MAX_PUISSANCE_HYDROGENE
        ) * 0.1
        candidate_score = objective(candidate_py, pd)

        if (candidate_score > best_score) and (MIN_PUISSANCE_HYDROGENE < candidate_py < MAX_PUISSANCE_HYDROGENE):
            py, best_score = candidate_py, candidate_score

        diff = candidate_score - curr_score

        t = temp / float(i + 1)

        sigmoid = 1 / (1 + exp(-diff / t))

        if sigmoid > 0.5:
            curr_py, curr_score = candidate_py, candidate_score

    return [py, best_score]