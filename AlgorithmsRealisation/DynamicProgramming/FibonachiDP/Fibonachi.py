# def fibonachi(n):
#     a1 = 1
#     a2 = 1
#     result = 0
#     for i in range(2, n):
#         result = a1 + a2
#         a2 = a1
#         a1 = result
#     return result

# top down (tabulation)
# def fibonachi(n):
#     array = [None] * (n + 1)
#     if array[n] == None:
#         if n <= 1:
#             array[n] = n
#         else:
#             array[n] = fibonachi(n - 1) + fibonachi(n - 2)
#     return array[n]

# bottom up (memorisation)
def fibonachi(n):
    array = [None] * (n + 1)
    array[0] = 0
    array[1] = 1
    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]
    return array[n]


print(fibonachi(9))
