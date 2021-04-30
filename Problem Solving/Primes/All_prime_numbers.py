"""All Prime Numbers"""
def is_prime(num):
    for i in range(2,num):
        if (num%i)==0:
            return False
    return True
def all_prime(num):
    primes = []
    for i in range(2,num+1):
        if is_prime(i) is True:
            primes.append(i)
    return primes
num = int(input("Enter a Number : "))
prime_no = all_prime(num)
print(prime_no)