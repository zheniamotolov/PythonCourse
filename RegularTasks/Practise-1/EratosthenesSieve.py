def eratosthenesSieve(n):
    array = [0] * n
    for i in range(n):
        array[i] = i
    array[1] = 0
    m = 2
    while m < n:
        if array[m] != 0:
            j = m ** 2
            while j < n:
                array[j] = 0
                j += m
        m += 1
    primeArray = []
    for i in array:
        if array[i] != 0:
            primeArray.append(array[i])
