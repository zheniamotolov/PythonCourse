# 1
myEnglishName = "eugeneolegovichmotolov"
myRussinaName = "евгенийолеговичмотолов"  # (input("enter you full name"))
arrayOfCharatersRu = list(myRussinaName)
arrayOfCharatersEn = list(myEnglishName)
# 1
print("Russian name")
n = 4
aeoiArrayRu = [[] for i in range(n)]
j = 0
for i in arrayOfCharatersRu:
    if i == 'a':
        aeoiArrayRu[0].append(j)
    elif i == 'е':
        aeoiArrayRu[1].append(j)
    elif i == 'о':
        aeoiArrayRu[2].append(j)
    elif i == 'и':
        aeoiArrayRu[3].append(j)
    j += 1

j = 0
for i in aeoiArrayRu:
    if j == 0:
        print('a ', i, " ", len(i))
    if j == 1:
        print('е ', i, " ", len(i))
    if j == 2:
        print('о ', i, " ", len(i))
    if j == 3:
        print('и ', i, " ", len(i))
    j += 1

print("English name")
n = 6
aeiouyArrayEn = [[] for i in range(n)]
j = 0
for i in arrayOfCharatersEn:
    if i == 'a':
        aeiouyArrayEn[0].append(j)
    elif i == 'e':
        aeiouyArrayEn[1].append(j)
    elif i == 'i':
        aeiouyArrayEn[2].append(j)
    elif i == 'o':
        aeiouyArrayEn[3].append(j)
    elif i == 'u':
        aeiouyArrayEn[2].append(j)
    elif i == 'y':
        aeiouyArrayEn[3].append(j)

    j += 1

j = 0
for i in aeiouyArrayEn:
    if j == 0:
        print('a ', i, " ", len(i))
    if j == 1:
        print('e ', i, " ", len(i))
    if j == 2:
        print('i ', i, " ", len(i))
    if j == 3:
        print('o ', i, " ", len(i))
    if j == 2:
        print('u ', i, " ", len(i))
    if j == 3:
        print('y ', i, " ", len(i))
    j += 1
