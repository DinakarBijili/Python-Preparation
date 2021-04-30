"""Decimal to binary (recursive)"""

def dec_to_binary(n):
    if n > 1:
        dec_to_binary(n//2)
    print(n%2, end=" ")
num = int(input("Enter a Decimal Value : "))
binary = dec_to_binary(num)