"""Password with Requirements [Premium]"""
import random
import string

def randomPassword(size):
    all_char = string.ascii_letters + string.digits+string.punctuation
    password = ""
    password +=random.choice(string.ascii_uppercase)
    password +=random.choice(string.ascii_lowercase)
    password +=random.choice (string.digits)
    password +=random.choice (string.punctuation)
    for i in range(size-4):
        password+=random.choice(all_char)
    return password

pass_len = int(input("what would be the password length : "))
print("First Randow password : ",randomPassword(pass_len))
print("Second Randow password : ",randomPassword(pass_len))
print("Third Randow password : ",randomPassword(pass_len))