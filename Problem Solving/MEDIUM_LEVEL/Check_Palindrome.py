""" Check palindrom e.g..,madam reverse madam """
str = input("Check palindrom : ")
rev_str = str [::1]
if str == rev_str:
    print("Its Palindrom")
else:
    print("Its not a Palindrom")

