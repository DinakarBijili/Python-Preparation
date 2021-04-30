"""Armstrong NUmber E.g..., 153 is a armstrong """
def armstrong(num):
    order = len(str(num))

    sum = 0 
    # use temp to find each digit. Then power it
    temp = num  
    while temp > 0:
        digit = temp % 10 
        sum += digit ** order
        temp //= 10 #If two operands have the same identity, it returns True. 
    return num == sum 


num = int(input("Enter a number : "))

if armstrong(num):
    print(num,"is a Armstrong")
else:
    print(num,"is not a Armstrong")