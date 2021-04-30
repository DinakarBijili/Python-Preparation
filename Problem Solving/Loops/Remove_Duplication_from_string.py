"""Remove Duplication from a String """
def remove_duplication(your_str):
    result = "" 
    for char in your_str:
       if char not in result:
           result += char
    return result
user_input = input("Enter Characters : ")
no_duplication = remove_duplication(user_input)
print("With out Duplication = ",no_duplication)

