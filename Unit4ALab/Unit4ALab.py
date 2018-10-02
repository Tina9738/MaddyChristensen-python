def main():
    #word = input ("Give me a word.")

    list1=[1, 2, 3, 4]
    x=7
    list2=mathStuff(list1, x)
    print (list2)




#def deVowel(word):
    #mylist=word
    #noVowel=''
    #for letter in word:
        #if(letter)==a or e or i or o or u:



def mathStuff(list1, x):
    for stuff in list1:
        list1.append(stuff*x)
        return (list1)



main()
