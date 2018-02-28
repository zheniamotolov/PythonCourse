# import EratosthenesSieve import eratosthenesSieve

N = round(float(input("enter N ")))
n = int(input("enter n "))


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
    return primeArray


primearray = eratosthenesSieve(N)

for i in range(1, n + 1):
    print("Power of ", i)
    for item in primearray:
        print(item ** i, " ", end='')
    print(end='\n')
