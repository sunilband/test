ip=int(input("what do you want to do? 1:add 2:sub 3:mul \n"))
a=int(input("enter value 1"))
b=int(input("enter value 2"))

def calc(a,b):
    if ip==1:
        print (a+b)
    elif ip==2:
        print (a-b)
    elif ip==3:
        print (a*b)
    else:
        print("enter valid choice")

calc(a,b)
