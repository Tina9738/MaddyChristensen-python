def main():
    shoppingCart=[["toothpaste", "q-tips", "milk"], ["milk", "candy", "apples"], ["paper", "pencils", "q-tips"]]
    print(allinOne(shoppingCart))

    metalBasket=[["Q-tips", 'water', "eggs"],["Chicken", "candy", "Q-tips"],["Gift", "Cheese", "Q-tips"]]
    print(countQtips(metalBasket))




def allinOne(Cart):

    print(Cart)
    Shopping=[]
    for list in Cart:
        for items in list:
            if items not in Shopping:
                Shopping.append(items)
    print(Shopping)

def countQtips(Basket):
    count=0
    for lists in Basket:
        for items in lists:
            if items=="Q-tips":
                count=count+1
    print("You have "+str(count) +" Qtips!")














main()
