while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    x = input("Please press number correlating to option desired: ")

    if x == "1":
        n1 = int(input("Enter first number of operation: "))
        n2 = int(input("Enter second number of operation: "))
        print("The answer is:", n1+n2)

    elif x == "2":
        n1 = int(input("Enter first number of operation: "))
        n2 = int(input("Enter second number of operation: "))
        print("The answer is: ", n1-n2)

    elif x == "3":
        n1 = int(input("Enter first number of operation: "))
        n2 = int(input("Enter second number of operation: "))
        print("The answer is: ", n1*n2)

    elif x == "4":
        n1 = int(input("Enter first number of operation: "))
        n2 = int(input("Enter second number of operation: "))
        print("The answer is: ", n1/n2)

    elif x == "5":
        break