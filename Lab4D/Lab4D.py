def main():
    shoppingCart=[["toothpaste", "q-tips", "milk"], ["milk", "candy", "apples"], ["paper", "pencils", "q-tips"]]
    print(allinOne(shoppingCart))

    metalBasket=[["Q-tips", 'water', "eggs"],["Chicken"] ]




def allinOne(Cart):

    print(Cart)
    Shopping=[]
    for list in Cart:
        for items in list:
            if items not in Shopping:
                Shopping.append(items)
    print(Shopping)

def countQtips(Basket):
    for lists in Basket:
        for items in Basket:










main()
