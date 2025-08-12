
"""
a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))


#a = int(a)
#b = int(b)

print(f"Sum of {a} and {b} is {a+b}")
"""



sid1 = input("Enter student id1:")
sid2 = input("Enter student id2:")

if (sid1.isnumeric()):
    sid1 = int(sid1)
else:
    print("Invalid Student Id or Student Id should be Numeric")
    exit(-1)

sname1 = input("Enter student name1:")
englishmark1 = int(input("Enter english mark:"))
sciencemark1 = int(input("Enter science mark:"))
mathsmark1 = int(input("Enter maths mark:"))

if (sid2.isnumeric()):
    sid2 = int(sid2)
else:
    print("Invalid Student Id or Student Id should be Numeric")
    exit(-1)
sname2 = input("Enter student name2:")
englishmark2 = int(input("Enter english mark:"))
sciencemark2 = int(input("Enter science mark:"))
mathsmark2 = int(input("Enter maths mark:"))


totalmarks1 = englishmark1 + sciencemark1 + mathsmark1
totalmarks2 = englishmark2 + sciencemark2 + mathsmark2
print("=============Student Info=================")
print(f"Student Id: {sid1}")
print(f"Student Name: {sname1}")
print(f"English Mark: {englishmark1}")
print(f"Science Mark: {sciencemark1}")
print(f"Maths Mark: {mathsmark1}")
print(f"Total Marks: {totalmarks1}")
print("==========================================")
if totalmarks1 >170:
    print("Your total marks is", totalmarks1,"pass")
else:
    print("Your total marks is", totalmarks1,"fail")

print("=============Student Info=================")
print(f"Student Id: {sid2}")
print(f"Student Name: {sname2}")
print(f"English Mark: {englishmark2}")
print(f"Science Mark: {sciencemark2}")
print(f"Maths Mark: {mathsmark2}")
print(f"Total Marks: {totalmarks2}")
print("==========================================")
if totalmarks2 > 170:
        print("Your total marks is", totalmarks2, "pass")
else:
        print("Your total marks is", totalmarks2, "fail")

# Updated comparison to print only the higher marks
if totalmarks1 > totalmarks2:
    print(f"Student with {sname1,totalmarks1} is higher")
elif totalmarks2 > totalmarks1:
    print(f"Student with {sname2, totalmarks2} is higher")
else:
    print(f"Both students have equal marks: {totalmarks1}")



