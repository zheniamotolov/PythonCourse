from itertools import permutations
from math import inf

best_route = None
best_coast = inf
graph = [[0, 4, 2, 1], [4, 0, 13, 9], [2, 13, 0, 8], [1, 9, 8, 0]]


def brute_force(route):
    global best_coast
    global best_route
    i = 0
    temp_cost = 0
    while i < len(route) - 1:
        temp_cost += graph[route[i]][route[i + 1]]
        i += 1
    temp_cost += graph[route[i]][0]
    temp_cost += graph[0][route[0]]
    if temp_cost < best_coast:
        best_coast = temp_cost
        best_route = route


def travelling_salesman():
    num_of_vertex = len(graph)
    routes = list(permutations(range(1, num_of_vertex)))

    for i in routes:
        brute_force(i)
    # print(routes)


def calculate_distance(route_point):
    route_coast = 0
    for i in route_point:
        route_coast += i
    return route_coast


def main():
    travelling_salesman()
    print(best_coast)
    print("0,", ', '.join(map(str, best_route)), ", 0")


if __name__ == "__main__":
    main()
