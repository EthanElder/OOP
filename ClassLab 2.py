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
        c = int(input("Enter the score of Lab 1 out of 10: "))
        e = int(input("Enter the score of Lab 2 out of 10: "))
        g = int(input("Enter the score of Lab 3 out of 10: "))
        m = int(input("Enter the score of Lab 4 out of 10: "))
        n = int(input("Enter the score of Lab 5 out of 10: "))
        x = c+e+g+m+n
        q = x*2
        w = x/5
        myDictionary.update({f:{
                                "name":b,
                                "Lab 1":c,
                                "Lab 2":e,
                                "Lab 3":g,
                                "Lab 4":m,
                                "Lab 5":n,
                                "Total Points":x,
                                "Percent Scored":q,
                                "Average Score per Lab":w
        }})

    elif a == 2:
        d = input("Please enter the student id (i.e. s1) to delete: ")
        del myDictionary[d]

    elif a == 3:
        h = input("Enter the student id: ")
        p = input("Enter the new student name: ")
        o = int(input("Enter the new score of Lab 1 out of 10: "))
        i = int(input("Enter the new score of Lab 2 out of 10: "))
        u = int(input("Enter the new score of Lab 3 out of 10: "))
        y = int(input("Enter the new score of Lab 4 out of 10: "))
        t = int(input("Enter the new score of Lab 5 out of 10: "))
        l = o+i+u+y+t
        k = l*2
        j = l/5
        myDictionary.update ({h:{
            "name":p,
            "Lab 1":o,
            "Lab 2":i,
            "Lab 3":u,
            "Lab 4":y,
            "Lab 5":t,
            "Total Points":l,
            "Percent Scored":k,
            "Average Score per Lab":j
        }})

    elif a == 4:
        print(myDictionary)

    elif a == 5:
        break