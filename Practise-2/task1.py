myName = "евгенийолеговичмотолов"  # (input("enter you full name"))
arrayOfCharaters = list(myName)

#1
aeoiArray = [0] * 4
for i in arrayOfCharaters:
    if i == 'a':
        aeoiArray[0] += 1
    elif i == 'е':
        aeoiArray[1] += 1
    elif i == 'о':
        aeoiArray[2] += 1
    elif i == 'и':
        aeoiArray[3] += 1

print(aeoiArray)
