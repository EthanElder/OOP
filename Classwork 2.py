a = int(input("Enter first random value: "))
b = int(input("Enter second random value: "))
c = int(input("Enter third random value: "))

if a>b and a>c:
    print("First value is the greatest")

elif a<b and b>c:
    print("Second value is the greatest")

else:
    print("Third value is the greatest")