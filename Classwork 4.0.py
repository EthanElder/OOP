myList = [25,58,64]

myList.append(10)
myList[2] = 59
myList[1] = 45
x = input("Enter your name: ")
myList.append(x)

for i in range (0, len(myList)):
    print(myList[i])

print(myList)