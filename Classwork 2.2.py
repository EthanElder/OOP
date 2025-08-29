class1 = int(input("Enter grade for class 1: "))
class2 = int(input("Enter grade for class 2: "))
class3 = int(input("Enter grade for class 3: "))
class4 = int(input("Enter grade for class 4: "))
class5 = int(input("Enter grade for class 5: "))

total = class5+class4+class1+class2+class3
total_percent = total/5

if total_percent<100 and total_percent>89:
    print("Grade A")

elif total_percent<90 and total_percent>79:
    print("Grade B")

elif total_percent<80 and total_percent>69:
    print("Grade C")

elif total_percent<70 and total_percent>59:
    print ("Grade D")

else:
    print("Grade F")