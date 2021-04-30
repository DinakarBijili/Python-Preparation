""" Calculate Grades"""
print("ENTER YOUR MARKS :-")
sub_1 = int(input("Enter Your 1st Subject Marks : "))
sub_2 = int(input("Enter Your 1st Subject Marks : "))
sub_3 = int(input("Enter Your 1st Subject Marks : "))
sub_4 = int(input("Enter Your 1st Subject Marks : "))
sub_5 = int(input("Enter Your 1st Subject Marks : "))

avg = (sub_1+sub_2+sub_3+sub_4+sub_5)/5
print("Average",avg)
if avg >= 90:
    print ("A Grade")
elif avg >=80:
    print("B Grade")
elif avg >=70:
    print("C Grade")
elif avg >=60:
    print("D Grade")
elif avg >=50:
    print("E Grade")
else:
    print("FAIL")