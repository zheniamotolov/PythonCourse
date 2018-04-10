# Здесь использован стпенная функция для понижения температуры
import json
import numpy as np
import random
import math
from copy import deepcopy

best_route = None
best_coast = None
start_temperature = 10000
final_temperature = 1
graph = 0  # [[0, 4, 2, 1], [4, 0, 13, 9], [2, 13, 0, 8], [1, 9, 8, 0]]
N = 0


def decrease_tempreture(i):
    return start_temperature * 0.1 / i


def do_transit(probability):
    if probability > 1 or probability < 0:
        raise ValueError('this not would be happened')
    if random.random() > probability:
        return False
    else:
        return True


def get_transition_probability(dE, T):
    p = math.exp(dE / T)
    return p


def get_new_route_candidate(route):
    new_route = deepcopy(route)
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    if i > j:
        new_route[j:i + 1] = np.flipud(new_route[j:i + 1])
    else:
        new_route[i:j + 1] = np.flipud(new_route[i:j + 1])
    return new_route


def get_new_2_opt_route(route):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    if i > j:
        new_route = np.concatenate((route[:j], route[j: i][::-1], route[i:]))
    else:
        new_route = np.concatenate((route[:i], route[i: j][::-1], route[j:]))


def calculate_energy(route):
    i = 0
    temp_energy = 0
    while i < len(route) - 1:
        temp_energy += graph[route[i]][route[i + 1]]
        i += 1
    temp_energy += graph[route[i]][route[0]]
    return temp_energy


def execute_annealing_simulation():
    current_route = np.random.permutation(N)

    current_energy = calculate_energy(current_route)
    current_temperature = start_temperature
    i = 1
    while current_temperature > final_temperature:
        # regular annealing simulation without 2-opt
        # new_route_candidate = get_new_route_candidate(current_route)

        #  annealing simulation with 2-opt
        new_route_candidate = get_new_route_candidate(current_route)
        new_route_candidate_energy = calculate_energy(new_route_candidate)
        if new_route_candidate_energy < current_energy:
            current_energy = new_route_candidate_energy
            current_route = new_route_candidate
        else:
            p = get_transition_probability(current_energy - new_route_candidate_energy, current_temperature)
            if do_transit(p):
                current_energy = new_route_candidate_energy
                current_route = new_route_candidate
        current_temperature = decrease_tempreture(i)
        i += 1

    print(current_route)
    print(current_energy)


def read_data():
    with open("data.txt") as f:
        res = json.load(f)
    return res


def main():
    global graph
    global N
    graph = read_data()
    N = len(graph)
    execute_annealing_simulation()


if __name__ == '__main__':
    main()
