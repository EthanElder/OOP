myList = [1,2,3,4,5,6,7,8,9]

print(myList)

while 1:
    print("1. Append an element to the list")
    print("2. Remove an element from the list")
    print("3. Pop an element from the list")
    print("4. Replace an element in the list")
    print("5. Sort the elements in the list")
    print("6. Reverse the elements in the list")
    print("7. Display the list")
    print("8. Quit")

    x = int(input("Enter your choice: "))
    if x == 1:
        y = int(input("Give number to append to list: "))
        myList.append(y)

    elif x == 2:
        a = int(input("Enter number in list to remove from list: "))
        myList.remove(a)

    elif x == 3:
        print("Last added number has been popped from list")
        myList.pop()

    elif x == 7:
        print(myList)

    elif x == 8:
        quit()

    elif x == 4:
        b = int(input("Enter the index of the number to replace: "))
        new = int(input("Enter a number to replace the previous number: "))
        myList[b] = new

    elif x == 5:
        myList.sort()
        print("List has been sorted into numeric order")

    elif x == 6:
        myList.reverse()
        print("List has been reversed")