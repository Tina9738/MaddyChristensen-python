def main():
    print("Bellarmine Student Average Current Grade")

    x=input ("Put in your grade:")
    year=whatYear(int(x))

    print ("You're a "+str(year) + "!")

    num=input("How many grades are you giving me?")
    list1=[0]*int(num)
    for grades in range(0,int(num)):
        print(grades)
        list1[grades]=int(input("Grade:"))
    print(list1)
    myGrade = averageGrade(list1)


    print("Your average grade is " + str(myGrade))

    print(letterGrade(myGrade))

    print(finalGrade(myGrade))

def whatYear (grade):
    int(grade)
    if grade==9:
        yourAnswer="freshman"
    elif grade==10:
        yourAnswer="sophmore"
    elif grade==11:
        yourAnswer="junior"
    elif grade==12:
        yourAnswer="senior"
    else:
        yourAnswer="not a high schooler!"
    return yourAnswer



def averageGrade(mylist):
    print("averageGrade")
    totalGrade=0
    for i in mylist:
        totalGrade=totalGrade+i
    averagegrade=totalGrade/ len(mylist)
    return averagegrade

def letterGrade(y):
    if y>=90:
        print("You have an A!")
    elif y>=80:
        print ("You have a B!")
    elif y>=70:
        print ("You have a C!")
    elif y>=60:
        print ("You have a D!")
    else:
        print ("You have an F.")
    return y


def finalGrade(z):
    if z>=60:
        print ("Congrats! You're passing!")
    else:
        print ("You're failing. You need to work harder.")
    return z
main()
