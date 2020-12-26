def Login():
    for x in range(3):
        name = str(input("Enter your name: "))
        surname = str(input("Enter your surname: "))
        if name=="Buse" and surname=="Yalcin":
            print("HOSGELDINIZ..")
            check = True
            break
        else:
            print("Please try again!!!!")
Login()

def Puan():
    sayi = int(input("How many lessons do you take? : "))

    if sayi<3:
        print ("YOU FAILED THE CLASS :( ")

    elif sayi==3:
        lesson1 = str(input("Enter your lesson: "))
        lesson2 = str(input("Enter your lesson: "))
        lesson3 = str(input("Enter your lesson: "))
        lessons = {lesson1, lesson2, lesson3}
        print (lessons)
        choise = int(input("Choise your exam key"))
        print("Your choise: ", choise)
        arasinav = int(input("Enter yoour arasinav point :"))
        final = int(input("Enter yoour final point: "))
        project = int(input("Enter yoour project point: "))
        points = {arasinav, final, project}
        print (points)
        point=(arasinav*0.3+final*0.5+project*0.2)
        print ("Your Final Point is: ",point)
        if point > 90:
            print ("AA")
        elif (point > 70 and point < 90):
            print("BB")
        elif (point > 50 and point < 70):
            print("CC")
        elif (point > 30 and point < 50):
            print("DD")
        else:
            print ("FF")

    elif sayi==4:
        lesson1 = str(input("Enter your lesson: "))
        lesson2 = str(input("Enter your lesson: "))
        lesson3 = str(input("Enter your lesson: "))
        lesson4 = str(input("Enter your lesson: "))
        lessons = {lesson1, lesson2, lesson3, lesson4}
        print (lessons)
        choise = int(input("Choise your exam key"))
        print("Your choise: ", choise)
        arasinav = int(input("Enter yoour arasinav point :"))
        final = int(input("Enter yoour final point: "))
        project = int(input("Enter yoour project point: "))
        points = {arasinav, final, project}
        print (points)
        point=(arasinav*0.3+final*0.5+project*0.2)
        print ("Your Final Point is: ", point)
        if point > 90:
            print ("AA")
        elif (point > 70 and point < 90):
            print("BB")
        elif (point > 50 and point < 70):
            print("CC")
        elif (point > 30 and point < 50):
            print("DD")
        else:
            print ("FF")

    else:
        lesson1 = str(input("Enter your lesson: "))
        lesson2 = str(input("Enter your lesson: "))
        lesson3 = str(input("Enter your lesson: "))
        lesson4 = str(input("Enter your lesson: "))
        lesson5 = str(input("Enter your lesson: "))
        lessons={lesson1,lesson2,lesson3,lesson4,lesson5}
        print (lessons)
        choise = int(input("Choise your exam key"))
        print("Your choise: ",choise)
        arasinav = int(input("Enter yoour arasinav point :"))
        final = int(input("Enter yoour final point: "))
        project = int(input("Enter yoour project point: "))
        points = {arasinav, final, project}
        print (points)
        point=(arasinav*0.3+final*0.5+project*0.2)
        print ("Your Final Point is: ", point)
        if point > 90:
            print ("AA")
        elif (point > 70 and point < 90):
            print("BB")
        elif (point > 50 and point < 70):
            print("CC")
        elif (point > 30 and point < 50):
            print("DD")
        else:
            print ("FF")
Puan()