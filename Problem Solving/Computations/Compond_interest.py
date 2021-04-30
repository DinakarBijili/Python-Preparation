"""Compond Interest """
def compond_interest(principal,rate,time):
    interest = principal * (1+rate/100)**time
    return interest
principal = float("Borrowed Money : ")
interest_rate = float("Interest rate : ")
time = float(input("Overall Duration : "))
due_money = compond_interest(principal,interest_rate,time)
print("Interest amount is ",due_money)