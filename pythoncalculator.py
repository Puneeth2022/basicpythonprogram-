#add
def add(num1, num2):
    return num1+num2
#subtract
def subtarct(num1, num2):
    return num1-num2
#multiply
def multiply(num1, num2):
    return num1*num2
#division
def division(num1, num2):
    return num1/num2

print("WELCOME TO PYTHON CALCULATOR\n")
operators={
    "+": add,
    "-": subtarct,
    "*":multiply,
    "/":division
}

num1=int(input("enter the first number\n"))
num2=int(input("enter the second number\n"))
for oprator in operators:
    print(oprator)
selected = input("select the option\n")
option=operators[selected]
result=option(num1,num2)
print(f"{num1} {selected} {num2} = {result}")