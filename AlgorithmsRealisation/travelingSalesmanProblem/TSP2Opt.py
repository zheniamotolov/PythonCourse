import numpy as np

best_route = None
best_coast = 0
start_temperature = 10000
final_temperature = 1
graph = [[0, 4, 2, 1], [4, 0, 13, 9], [2, 13, 0, 8], [1, 9, 8, 0]]
N = len(graph)

# def do_2_opt_improved(route):
#     global best_coast
#     global best_route
#     for ci in range(0, N):
#         for xi in range(0, N):
#             yi = (ci + 1) % N
#             zi = (xi + 1) % N
#             c = route[ci]
#             y = route[yi]
#             x = route[xi]
#             z = route[zi]
#
#             cy = graph[route[c]][route[y]]
#             yz = graph[route[y]][route[x]]
#             cx = graph[route[c]][route[x]]
#             xz = graph[route[x]][route[z]]
#
#             if xi != ci and xi != yi:
#                 current_coast = (cy + xz) - (cx + yz)
#                 if current_coast > best_coast:
#                     best_coast = current_coast
#                     best_route = (ci, yi, xi, zi)
#
#     if best_route is not None:
#         (ci, yi, xi, zi) = best_route
#         new_route = np.arange(0, N)
#         new_route[0] = route[ci]
#         n = 1
#
#         while xi != yi:
#             new_route[n] = route[xi]
#             n = n + 1
#             xi = (xi - 1) % N
#         new_route[n] = route[yi]
#
#         n = n + 1
#         while zi != ci:
#             new_route[n] = route[zi]
#             n = n + 1
#             zi = (zi + 1) % N
#         print(new_route)
#         print(best_coast)
#     else:
#         print(route)
#         print(best_coast)

####################################################

def calculate_coast(route):
    i = 0
    temp_coast = 0
    while i < len(route) - 1:
        temp_coast += graph[route[i]][route[i + 1]]
        i += 1
    temp_coast += graph[route[i]][route[0]]
    return temp_coast


def do_algorithm(current_path):
    global best_route
    global best_coast
    for i in range(0, N):
        for j in range(i + 1, N):
            new_route = np.concatenate((current_path[:i], current_path[i: j][::-1], current_path[j:]))
            new_route_coast = calculate_coast(new_route)
            if new_route_coast < best_coast:
                best_coast = new_route_coast
                best_route = new_route
                return True
    return False


def do_2_optimal():
    global best_coast
    current_path = np.arange(N)
    best_coast = calculate_coast(current_path)
    update_possible = do_algorithm(current_path)
    while update_possible and best_coast > 0:
        update_possible = do_algorithm(current_path)
    print(best_route)
    print(best_coast)


def main():
    do_2_optimal()
    # do_2_opt_improved(np.arange(N))

if __name__ == '__main__':
    main()
