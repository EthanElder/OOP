myList = [1,2,3,4,5,6,7,8,9]

print(myList)

while 1:
    print("1. Append to the list")
    print("2. Remove from the list")
    print("3. Pop element from the list")
    print("4. Display the list")
    print("5. Quit")

    x = int(input("Enter your choice: "))
    if x == 1:
        y = input("Give number to append to list: ")
        myList.append(y)

    elif x == 2:
        a = input("Enter number in list to remove from list: ")
        myList.remove(a)

    elif x == 3:
        print("Last added number has been popped from list")
        myList.pop()

    elif x == 4:
        print(myList)

    elif x == 5:
        quit()
