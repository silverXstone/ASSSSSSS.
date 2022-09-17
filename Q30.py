A=int(input("Enter first value:-"))
B=int(input("Enter second value:-"))
A = (A&B)+(A|B)
B = A+(~B)+1
A=A+(~B)+1
print("B after swapping:-",A)
print("B after swapping:-",B)
