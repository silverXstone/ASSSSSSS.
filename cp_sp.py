sp = int(input("Enter the selling price of the product:-"))
cp = int(input("Enter the cost price of the product:-"))
if sp>cp:
    a=sp-cp
    print("Profit on selling the product=",a)
else:
    print("You got loss=",cp-sp)
