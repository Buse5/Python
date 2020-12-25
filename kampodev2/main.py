#2.gun odevi
name = str(input("Please enter your name: "))
surname = str(input("Please enter your surname: "))
age = int(input("Please enter your age: "))
date = str(input("Please only enter your year of birth: "))

mylist = [name,surname,age,date]

for i in mylist:
  print(i)
if age<18:
    print ("You can't go out because it is too dangerous")
else:
    print ("You can go out to the street")