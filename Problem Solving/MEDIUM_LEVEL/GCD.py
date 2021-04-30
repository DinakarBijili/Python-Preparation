
"""GCD (Greater common divisor)"""
def gcd(x,y):
    smallest = min(x,y)

    gcd = 1
    for i in range(1,smallest+1):
        if (x%i == 0 ) and (y%i==0):
            gcd = i
    return gcd
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))

result = gcd(num1,num2)
print("GCF of ",num1,"and",num2 ,"is",result )

#OTHER METHOD
# import math
# num1 = int(input("Enter 1st Number : "))
# num2 = int(input("Enter 2nd Number : "))
# gcd = math.gcd(num1,num2)
# print(gcd)