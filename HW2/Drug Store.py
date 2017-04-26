shop = ["Cocaine","LCD","Heroine"]
n = input ("Welcome to our shop, what do you want(C,R,U,D)?:")
if n == "C":
    m = input ("New Items ?")
    shop.append (m)
    print ("Our Items",shop)

elif n == "R":
    print ("Our Items",shop)

elif n == "U":
    a = int(input("Update Position ?"))
    b = input("New items?")
    shop.insert(a, b)
    print ("Our Items",shop)
elif n == "D":
    delete = int(input("Delete position?"))
    shop.pop(delete)
    print("Our items:", shop)
else:
    print("Syntax Erros...")
