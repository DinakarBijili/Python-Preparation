
"""Sum of Squares"""
def sum_of_squares(n):
    sum = n*(n+1)*(2*n+1)
    return sum
num = int(input("Enter a number : "))
result = sum_of_squares(num)
print(result)