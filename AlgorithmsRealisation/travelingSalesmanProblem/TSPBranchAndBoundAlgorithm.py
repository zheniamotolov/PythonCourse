from math import inf
from heapq import nsmallest
import numpy as np

best_route = []
best_coast = inf
graph = np.array([
    [inf, 90, 80, 40, 100], [60, inf, 40, 50, 70], [50, 30, inf, 60, 20], [10, 70, 20, inf, 50], [20, 40, 50, 20, inf]
])
visited_vertexes = None
num_of_vertex = len(graph)
lower_bound = 0


def execute_branch_and_bound_algorithm():
    global lower_bound
    sum_ij = 0
    sum_ij += subtract_min_from_row()
    sum_ij += subtract_min_from_column()
    lower_bound += sum_ij
    simplify_matrix()
    print(lower_bound)


# def reduce_matrix():


def simplify_matrix():
    global graph
    global lower_bound
    global num_of_vertex
    global best_route
    temp_max_sum_ij = 0

    max_i = None
    max_j = None
    i = 0
    j = 0
    while i < num_of_vertex:
        while j < num_of_vertex:
            if graph[i][j] == 0:
                temp_column = graph[:, j]
                temp_column = np.delete(temp_column, i)
                temp_row = graph[i]
                temp_row = np.delete(temp_row, j)
                current_sum_ij = temp_column.min() + temp_row.min()

                if temp_max_sum_ij < current_sum_ij:
                    temp_max_sum_ij = current_sum_ij
                    max_i = i
                    max_j = j
            j += 1
        j = 0
        i += 1
    num_of_vertex -= 1
    temp_lower_bound = reduce_matrix(max_i, max_j)
    if temp_lower_bound > temp_max_sum_ij:
        # lower_bound -= temp_lower_bound
        lower_bound += temp_max_sum_ij
    best_route.append(max_i)
    best_route.append(max_j)


def reduce_matrix(max_i, max_j):
    global graph
    graph = np.delete(graph, max_i, 0)
    graph = np.delete(graph, max_j, 1)
    print("keks")
    print(graph)
    sum_ij = 0
    sum_ij += subtract_min_from_row()
    sum_ij += subtract_min_from_column()
    return sum_ij

    # sum_ij = 0
    # i = 0
    # j = 0
    # while i < num_of_vertex:
    #     min_row = nsmallest(1, graph[i])[-1]
    #     sum_ij += min_row
    #     graph[i] = list(map(lambda v: v - min_row, graph[i]))
    #     i += 1
    # while i < num_of_vertex:
    #     while j < num_of_vertex:
    #         # if graph[i][j] == 0:
    #         #     j += 1
    #         #     continue
    #         # else:
    #
    #         #     temp_column = graph[:, j]
    #         #     temp_column = np.delete(temp_column, i)
    #         #     temp_row = graph[i]
    #         #     temp_row = np.delete(temp_row, j)
    #         #     sum_ij += temp_column.min() + temp_row.min()
    #             j += 1
    #     j = 0
    #     i += 1
    # print(sum_ij)


def subtract_min_from_column():
    global graph
    sum_ij = 0
    j = 0
    while j < num_of_vertex:
        min_column = nsmallest(1, graph[:, j])[-1]
        sum_ij += min_column  # change
        graph[:, j] = list(map(lambda v: v - min_column, graph[:, j]))
        j += 1
    print(graph)
    return sum_ij


def subtract_min_from_row():
    global graph
    sum_ij = 0
    i = 0
    while i < num_of_vertex:
        min_row = nsmallest(1, graph[i])[-1]
        sum_ij += min_row  # change
        graph[i] = list(map(lambda v: v - min_row, graph[i]))
        i += 1
    print(graph)
    return sum_ij


def execute_travelling_salesman():
    execute_branch_and_bound_algorithm()


def main():
    execute_travelling_salesman()


if __name__ == "__main__":
    main()
