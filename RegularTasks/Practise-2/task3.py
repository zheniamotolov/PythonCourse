# 3,4
myEnglishName = "eugeneolegovichmotolov"
myRussinaName = "евгенийолеговичмотолов"  # (input("enter you full name"))

myEnglishPatronum = myEnglishName
myRussinaPatronum = myRussinaName[7:15]
russinEnglishPatronum = myEnglishPatronum + myRussinaPatronum
print(russinEnglishPatronum)

russianEnglishNameSurname = myRussinaName[:7] + myRussinaName[15:] + myEnglishName[:6] + myEnglishName[15:]
print(russianEnglishNameSurname)

for i in "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя":
    if 0 < russianEnglishNameSurname.count(i) <= 2:
        russinEnglishPatronum += i
print(russinEnglishPatronum)
