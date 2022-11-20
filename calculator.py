num_1=int(input("enter 1st number"))
num_2=int(input("enter 2st number"))

def add(num_1,num_2):
    return num_1+num_2
def sub(num_1,num_2):
    return num_1-num_2
def mul(num_1,num_2):
    return num_1*num_2
def div(num_1,num_2):
    return num_1/num_2

print("select which operation you want to perform:-")
print("a for addition")
print("s for substraction")
print("m for multiplication")
print("d for division")

ch=input("enter your choice a / s / m / d :-\n")

if ch=='a':
    print(" addition of %d and %d  is \n"%(num_1,num_2),add(num_1,num_2))
elif ch=='s':
    print(" substraction of %d and %d  is \n"%(num_1,num_2),sub(num_1,num_2))
elif ch=='m':
    print(" multiplication of %d and %d  is \n"%(num_1,num_2),mul(num_1,num_2))
elif ch=='d':
    print(" division of %d and %d  is \n"%(num_1,num_2),div(num_1,num_2))
else:
    print("please enter valid input")


