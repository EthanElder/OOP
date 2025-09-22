Projects = {}
Managers = []
Technologies = []
Members = []

while 1:
    print("1. Start a new project")
    print("2. Remove a project")
    print("3. Project project update")
    print("4. Print specific project")
    print("5. Print all projects")
    print("6. Quit program")
    q = int(input("Enter your selection here: "))

    if q == 1:
        prjct_id = input("Enter the project id: ")
        title = input("Enter the project title: ")
        num = int(input("Enter the amount of managers to add: "))
        for i in range (0,num):
            Managers.append(input("Enter manager's name: "))
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        sponsor = input("Enter the project sponsor: ")
        budget = input("Enter the budget: ")
        tech_num = int(input("Enter the amount of tech items to add: "))
        for i in range (0,tech_num):
            Technologies.append(input("Enter the technology: "))
        members = int(input("Enter the amount of team members: "))
        for i in range (0,members):
            Members.append(input("Enter the team member's name: "))

        Projects.update({prjct_id:{
            "Title":title,
            "Managers":Managers,
            "Start":start_date,
            "Finish":end_date,
            "Sponsor":sponsor,
            "Budget":budget,
            "Technologies":Technologies,
            "Team Members":Members
        }})

    elif q == 2:
        deleter = input("Enter the id of the project you would like to delete: ")
        del Projects[deleter]

    elif q == 6:
        break

    elif q == 5:
        print(Projects)

    elif q == 3: