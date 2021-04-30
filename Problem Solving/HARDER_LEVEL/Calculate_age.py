"""Calculate age"""

from datetime import datetime

def calculate_age(born):
    today = datetime.today()
    days = (today-born).days
    age = days // 365
    return age 

def get_user_input():
 user_input =input("Enter you Birth Date in DD/MM/YYYY : ")
 try:
     birthday = datetime.strptime(user_input, "%d/%m/%Y")
 except TypeError:
     birthday = datetime.datetime(datetime.strptime(user_input,"%d/%m/%Y"[0:6]))
 return birthday

birthday = get_user_input()
age = calculate_age(birthday)
print("Your Age : ",age)