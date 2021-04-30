""" Password generator """
import random 
import string

def generate_password(size):
    all_char = string.ascii_letters+string.digits+string.punctuation
    password = " "
    for char in range(size):
        rand_char = random.choice(all_char)
        password = password + rand_char
    return password

#user input 
user_input = int(input("How many characters in your password : "))
new_password = generate_password(user_input)
print("New Password :",new_password)