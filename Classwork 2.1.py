a = int(input("Enter first value of operation: "))
b = int(input("Enter second value of operation: "))

op = input("Please enter operation sign: ")

if op == "+":
    print("The sum is:", a+b)

elif op == "-":
    print("The subtraction is:", a-b)

elif op == "*":
    print("The multiplication is:", a*b)

elif op == "/":
    print("The division is:", a/b)

else:
    print("Please enter a valid operation sign, ex. +, -, *, /")

