# 3x^4 + 5y^2 + 10z = 103 -- программа решает данноу уравнение до момента когда находит первое решение
import random

allele_size = 3
max = 1000000
a = 3
b = 5
c = 10
d = 103  # answer 76 # 3x + 5y + 10z = 76
parents_probability = [0] * max


def create_new_child(population, parent_1, parent_2):
    crossover = random.randint(1, 2)
    is_first_parent = random.randint(0, 101)
    child = population[parent_1]
    initial = 0
    final = 2
    if is_first_parent < 50:
        initial = crossover
    else:
        final = crossover + 1
    i = initial
    while i < final:
        child[i] = population[parent_2][i]
        if random.randint(0, 100) < 10:
            child[i] = random.randint(0, d)
        i += 1
    return child


def get_parent_probability(choose_probability):
    last = 0
    i = 0
    while i < max:
        if last <= choose_probability <= parents_probability[i]:
            return i
        else:
            last = parents_probability[i]
        i += 1

    return random.randint(0, max - 1)


def create_new_population(population):
    new_population = [[0] * 3 for i in range(max)]
    i = 0
    while i < max:
        parent_1 = 0
        parent_2 = 0
        iterations = 0
        while parent_1 == parent_2 or population[parent_1] == population[parent_2]:
            parent_1 = get_parent_probability(random.randint(0, 100) % 101)
            parent_2 = get_parent_probability(random.randint(0, 100) % 101)
            iterations += 1
            if iterations > max:
                break
        new_population[i] = create_new_child(population, parent_1, parent_2)
        i += 1


def count_population_fitness():
    # global population_fitness
    sum_of_alleles_fitness = sum(parents_probability)
    i = 0
    while i < max:
        parents_probability[i] = (parents_probability[i] / sum_of_alleles_fitness) * 100
        i += 1


def do_substitution_to_equation(allele):
    equation_value = a * (allele[0] ** 4) + b * (allele[1] ** 2) + c * allele[2]
    return abs(d - equation_value)


def count_fitness(populations):
    i = 0
    while i < max:
        fitness = do_substitution_to_equation(populations[i])
        if fitness == 0:
            return i
        parents_probability[i] = 1 / fitness
        i += 1
    return 0


def create_random_population(population):
    # allele_size = len(population)
    i = 0
    j = 0
    while i < max:
        while j < allele_size:
            population[i][j] = random.randint(0, d)
            j += 1
        j = 0
        i += 1

    fitness = count_fitness(population)
    if fitness:
        return population[fitness]

    iteration = 0
    while fitness != 0 or iteration < max:
        count_population_fitness()
        create_new_population(population)
        fitness = count_fitness(population)
        if fitness:
            return population[fitness]
        iteration += 1

    return -1


def initialize():
    population = [[0] * 3 for i in range(max)]
    # print(population)
    print(create_random_population(population))


def main():
    initialize()


if __name__ == '__main__':
    main()
