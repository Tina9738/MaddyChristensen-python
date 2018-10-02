def main():
    print("Bellarmine Student Average Current Grade")

    x=input ("Put in your grade:")
    year=whatYear(int(x))

    print ("You're a "+str(year) + "!")

    list1=[99, 92.7, 84.3, 90.7]
    myaverage=averageGrade(list1, len(list1))
    print("Your average grade is " + str(myaverage))

    print(letterGrade(myaverage))

    print(finalGrade(myaverage))

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



def averageGrade(mylist, x):
    totalGrade=mylist[0]+mylist[1]+mylist[2]+mylist[3]
    averagegrade=totalGrade/x
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
