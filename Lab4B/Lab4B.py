def main():
    list1=[1,2,3,4,5]
    times10(list1)

    list3=[10,20,30,40,50]
    print (multiples10(list3))




def times10(list2):
    for values in range (0, 5):
        print (values+10)
        print (values*10)




def multiples10(list4):
    for value in range (0, 4):
        list4.pop(value)
        list4+(value*10)

    return list4





main()
