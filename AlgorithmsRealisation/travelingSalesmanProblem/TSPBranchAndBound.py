from math import inf
from heapq import nsmallest

best_route = None
best_coast = inf
graph = [[0, 4, 2, 1], [4, 0, 13, 9], [2, 13, 0, 8], [1, 9, 8, 0]]
visited_vertexes = None
num_of_vertex = len(graph)

def find_first_min_edge(vertex):
    return nsmallest(2, graph[vertex])[-1]  # complexity is logk(k=2) not nlogn (in sort)!!!


def find_second_min_edge(vertex):
    return nsmallest(3, graph[vertex])[-1]


def execute_branch_and_bound_algorithm(current_bound, current_weight, level, current_path):
    # if level==num_of_vertex


def execute_travelling_salesman():
    global visited_vertexes

    route = (num_of_vertex + 1) * [-1]
    visited_vertexes = (num_of_vertex + 1) * [False]
    current_bound = 0

    i = 0
    while i < num_of_vertex:
        current_bound += ((find_first_min_edge(i) + find_second_min_edge(i)) / 0.5)
        i += 1
    visited_vertexes[0] = True
    route[0] = 0

    execute_branch_and_bound_algorithm(current_bound, 0, 1, route)
    print(route)
    print(visited_vertexes)


def main():
    execute_travelling_salesman()


if __name__ == "__main__":
    main()
