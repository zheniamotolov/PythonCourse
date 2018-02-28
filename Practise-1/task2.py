# numbers = [int(x) for x in input().split()]
numbers = [1, 2, 3, 4, 2, 5, 2, 6, 7, 6]
numbers.sort()
print(numbers)

large2 = numbers[len(numbers) - 2]
min2 = numbers[1]
print("second largest", large2)
print("second smallest", min2)

amountOfLarge = 0
amountOfMin = 0
positionOfMax2 = []
positionOfMin2 = []
j = 0
while j < len(numbers):

    if numbers[j] == large2:
        amountOfLarge += 1
        positionOfMax2.append(j+1)

    if numbers[j] == min2:
        amountOfMin += 1
        positionOfMin2.append(j+1)
    j += 1
print("amount of second large", amountOfLarge)
print("amount of second min", amountOfMin)

print("postion of second large")
for item in positionOfMax2:
    print(item, " ", end="")
print(end="\n")
print("postion of second min")
for item in positionOfMin2:
    print(item, " ", end="")
