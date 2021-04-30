"""LCM (Least common Multiple)"""
import math
num1 = int(input("Enter 1st Number : "))
num2 = int(input("Enter 2nd Number : "))
lcf = math.lcm(num1,num2)
print(lcf)

#OTHER METHOD
# def lcm_number(x,y):
#     lcm = max(x,y)
#     while lcm % x != 0 or lcm % y != 0:
#         lcm+=1
#     return lcm
# num1 = int(input("Enter 1st Number : "))
# num2 = int(input("Enter 2nd Number : "))
# result = lcm_number(num1,num2)

# print("LCG of",num1,"and",num2,"is",result)