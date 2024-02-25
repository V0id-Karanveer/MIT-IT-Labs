def mul(a,b):
    return a*b

def sub(a,b):
    return a-b

def add(a,b):
    return a+b

def div(a,b):
    return a/b

num1 = int(input("enter no1"))
num2 = int(input("enter no2"))
op = input("enter operator")

if (op=="+"):
    print(add(num1,num2))\
    
if (op=="*"):
    print(mul(num1,num2))

if (op=="/"):
    print(div(num1,num2))

if (op=="-"):
    print(sub(num1,num2))
