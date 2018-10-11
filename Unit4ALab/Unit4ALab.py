def main():
    input=("Give me a word.")
    print (deVowel (str(input)))


    list=[1, 2, 3, 4]
    y=7
    print (mathStuff(list,y))



def deVowel(word):
    mylist=''
    for letter in word:
        if letter=="a":
            mylist=mylist
        elif letter=="e":
            mylist=mylist
        elif letter=="i":
            mylist=mylist
        elif letter=="o":
            mylist=mylist
        elif letter=="u":
            mylist=mylist
        else:
            mylist=mylist+letter

    return (mylist)





def mathStuff(list1, x):
    newList=[]
    for values in list1:
        print (values)
        newList.append(int(values) * (x))


    return (newList)


main()
