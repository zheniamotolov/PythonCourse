numbers = [6, 3, 7, 4, 10, 9, 8, 6, 14]
# 5 2 7 4 0 9 8 6

NoProperty = "не обладает свойством монотонности"
IncreaseProperty = "возрастающая"
DecreaseProperty = "убывающая"
i = 1
moreThanPrevious = 0
lessThanPrevious = 0
while i < len(numbers):
    if numbers[i] > numbers[i - 1]:
        moreThanPrevious += 1
    else:
        lessThanPrevious += 1
    i += 1

print("количество элементов, больших предыдущего: ", moreThanPrevious)
print("количество элементов, меньше предыдущего: ", lessThanPrevious)

increasing = False
decreasing = False
monotonus = False

print(NoProperty)


# insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertionSort(numbers)
print("Sorted array is:")
for i in range(len(numbers)):
    print("%d" % numbers[i],end='')
print()

i = 0
k = 1
while i < len(numbers):
    for l in range(k):
        print(numbers[i], end="")
        i += 1
        if i >= len(numbers):
            break

    print(end="\n")
    k += 1
