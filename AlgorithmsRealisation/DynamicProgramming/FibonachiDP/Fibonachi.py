def fibonachi(n):
    a1 = 1
    a2 = 1
    result = 0
    for i in range(2, n):
        result = a1 + a2
        a2 = a1
        a1 = result
    return result

print(fibonachi(10))
