def main():
    #word = open
    #print (deVowel (str(word)))


    list1=[1, 2, 3, 4]
    x=7
    print (mathStuff(list1,x))


#def deVowel(word):
    #mylist=word
    #for letter in mylist:
        #if letter==o:
            #mylist.remove(str(letter))
        #elif letter==e:
            #mylist.remove(str(letter))
            #print (mylist)

    #return (mylist)





def mathStuff(list1, x):
    newList=[]
    for values in list1:
        print (values)
        newList.append(int(values) * (x))

        return (newList)


main()
