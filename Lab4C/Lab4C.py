def main():
    for i in range(0, 7):
        draw7()

def draw7():
       starString=''
       for i in range(0,7):
           starString += '*'

       print(starString)

main()

input ("pause")

def main2():
    for i in range (0,3):
        starsAndStripes()

def starsAndStripes():
    newFlag=''
    flagNew=""
    for i in range(0, 7):
        newFlag+= "*"
    print (newFlag)
    for j in range (0, 7):
        flagNew+= "-"
    print (flagNew)

main2()

input ("pause")

def main3():
    for i in range(0,1):
        incTriangle()

def incTriangle():
    for i in range(0,1):
        print ("1")
    for i in range(0,1):
        print ("22")
    for i in range(0,1):
        print ("333")
    for i in range(0,1):
        print ("4444")
    for i in range(0,1):
        print ("55555")
    for i in range(0,1):
        print ("666666")
    for i in range(0,1):
        print ("7777777")

main3()

print ("pause")

def increaseTriangle():
    for i in range(1,20):
        triString=""
        for j in range(0,i):
            triString+=str(i)
        print(triString)

increaseTriangle()


