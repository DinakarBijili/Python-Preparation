def count_char(str):
    result = {}
    for char in str:
        if char in result.keys():
            result[char] = result[char]+1
        else:
            result[char] = 1
    for keys,value in result.items():
        print(keys,"=",value)
s = input("Enter your string : ")
count_char(s)
