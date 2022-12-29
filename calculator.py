ip=int(input("what do you want to do? \n1:addition \n2:substract \n3:multipy \n4:divide\n Enter choice number\n"))
a=int(input("enter first value\n"))
b=int(input("enter second value\n"))

def calc(a,b):
    if ip==1:
        print (f"the addition of {a} and {b} is {a+b}")
    elif ip==2:
        print (f"the substraction of {a} and {b} is {a-b}")
    elif ip==3:
        print (f"the multiplication of {a} and {b} is {a*b}")
    elif ip==4:
        print (f"the division of {a} and {b} is {a+b}")
    else:
        print("enter valid choice")

calc(a,b)
