"""decimal to binary """
def decimal_to_binary(n):
    bits = []
    while n > 0:
        bits.append(n%2)
        n = n//2
    bits.reverse()
    binary = " "
    for bit in bits:
        binary+=str(bit)
    return binary
num = int(input("Enter a number : "))
binary = decimal_to_binary(num)
print("decimal to Binary =",binary)

