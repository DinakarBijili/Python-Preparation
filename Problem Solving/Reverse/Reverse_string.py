"""Reverse String """
def reverse_str(str):
    reverse = " "
    for i in str:
        reverse = i + reverse
    return reverse
char = input("Enter Characters you want to reverse : ")
result = reverse_str(char)
print("Reverse String =",result)
