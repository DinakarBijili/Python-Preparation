"""Divisible by 3 and 5 """
def divisible_by_3_and_5(num):
    result = [ ]
    for i in range(0,num):
        if i%3==0 and i%5==0:
            result.append(i)
    return result

if __name__=="__main":
    user_input = int(input("Enter a number : "))
    result = divisible_by_3_and_5(user_input)
    print(result)