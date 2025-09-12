name = []
age = []

print(name, age)

while 1:
    print("1. Append an element to the list")
    print("2. Remove an element from the list")
    print("3. Pop an element from the list")
    print("4. Replace an element in the list")
    print("5. Reverse the elements in the list")
    print("6. Display the list")
    print("7. Quit")

    x = int(input("Enter your choice: "))
    if x == 1:
        g = int(input("Enter '1' for age and '2' for name: "))
        if g == 1:
            y = int(input("Enter the age you would like to add: "))
            age.append(y)
        elif g == 2:
            p = input("Enter the name you would like to add: ")

    elif x == 2:
        a = int(input("Enter number in list to remove from list: "))
        age.remove(a)

    elif x == 3:
        print("Last added number has been popped from list")
        .pop()

    elif x == 6:
        print()

    elif x == 7:
        quit()

    elif x == 4:
        b = int(input("Enter the index of the number to replace: "))
        new = int(input("Enter a number to replace the previous number: "))
        [b] = new

    elif x == 5:
        .reverse()
        print("List has been reversed")