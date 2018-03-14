# 2
myEnglishName = "eugeneolegovichmotolov"
myRussinaName = "евгенийолеговичмотолов"  # (input("enter you full name"))
arrayOfCharatersRu = list(myRussinaName)
arrayOfCharatersEn = list(myEnglishName)

print("russian name")


def letterCheckRu(c):
    if c in 'аоиеёэыуюя':
        return '1'
    else:
        return '0'


binaryStringRu = ''.join(list(map(letterCheckRu, arrayOfCharatersRu)))
print(binaryStringRu)
resultingBinaryNumbersFromRuString = []


def findBinaryNumbers():
    global binaryStringRu
    for i in range(1, 100):
        sequenseBinaryNumber = bin(i)[2:]
        if sequenseBinaryNumber in binaryStringRu:
            binaryStringRu = binaryStringRu.replace(sequenseBinaryNumber, "", 1)
            resultingBinaryNumbersFromRuString.append(sequenseBinaryNumber)
            print(sequenseBinaryNumber, " ", int(sequenseBinaryNumber, 2))


findBinaryNumbers()

print(resultingBinaryNumbersFromRuString)



print("english name")


def letterCheckEn(c):
    if c in 'aeiyuo':
        return '1'
    else:
        return '0'


binaryStringEn = ''.join(list(map(letterCheckEn, arrayOfCharatersEn)))
print(binaryStringEn)
resultingBinaryNumbersFromEnString = []


def findBinaryNumbers():
    global binaryStringEn
    for i in range(1, 100):
        sequenseBinaryNumber = bin(i)[2:]
        if sequenseBinaryNumber in binaryStringEn:
            binaryStringEn = binaryStringEn.replace(sequenseBinaryNumber, "", 1)
            resultingBinaryNumbersFromEnString.append(sequenseBinaryNumber)
            print(sequenseBinaryNumber, " ", int(sequenseBinaryNumber, 2))


findBinaryNumbers()

print(resultingBinaryNumbersFromEnString)


def letterChanger(c):
    temp = ''
    if c in "abcdefghijklmnopqrstuvwxyz":
        temp = '3'
    if c in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        temp = '1'
    if c in "аекосхaekocx":
        temp = '2'
    return temp


EnRuNameArray = arrayOfCharatersEn + arrayOfCharatersRu

EnRuCarString = ''.join(list(map(letterChanger, EnRuNameArray)))
print(EnRuCarString)
# (А, В, Е, І, К, М, Н, О, Р, С, Т, Х)
# a e k o c x
