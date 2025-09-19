myDictionary = {}

while 1:
    print("1. Add student to the dictionary")
    print("2. Delete a student from the dictionary")
    print("3. Edit a student on the dictionary")
    print("4. Print the dictionary")
    print("5. Quit")

    a = int(input("Enter your choice: "))

    if a == 1:
        f = input("Enter the student id (i.e. s1): ")
        b = input("Enter the name of the student: ")
        c = input("Enter the major of the student: ")
        e = input("Enter the year of the student: ")
        g = float(input("Enter the gpa of the student: "))
        myDictionary.update({f:{
                                "name":b,
                                "major":c,
                                "year":e,
                                "gpa":g
        }})

    elif a == 2:
        d = input("Please enter the student id (i.e. s1) to delete: ")
        del myDictionary[d]

    elif a == 3:
        h = input("Enter the student id: ")
        p = input("Enter the new student name: ")
        o = input("Enter the new student major: ")
        i = input("Enter the new student year: ")
        u = float(input("Enter the new student gpa: "))
        myDictionary.update ({h:{
            "name":p,
            "major":o,
            "year":i,
            "gpa":u
        }})

    elif a == 4:
        print(myDictionary)

    elif a == 5:
        break