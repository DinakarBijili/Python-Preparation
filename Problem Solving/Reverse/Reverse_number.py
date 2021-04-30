"""Reverse Number"""
def reverse_num(num):
    reverse = 0
    while num > 0:
        last_digit = num%10
        reverse = reverse*10 + last_digit
        num = num//10
    return reverse

num = int(input("Enter Number "))
result = reverse_num(num)
print(result)