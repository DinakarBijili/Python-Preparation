""" Simple Calculator """
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
def mod(num1,num2):
    return num1 % num2

#Taking input from the User
num1 = int(input("Enter 1st Number : "))
operation = input("What you want to do (+,-.*,/,%) : ")
num2 = int(input("Enter 2nd Number : "))

result = 0 
if operation == "+":
    result = add(num1,num2)
elif operation == "-":
    result = sub(num1,num2)
elif operation == "*":
    result = mul(num1,num2)  
elif operation == "/":
    result = div(num1,num2)
elif operation == "%":
    result = mod(num1,num2)
else:
     print("Please enter: +, -, *, / or %")

print(num1, operation, num2, '=', result)
