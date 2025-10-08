class Student:
    def __init__(self):
        self.sid = ""
        self.stuname = ""
        self.major = ""
        self.gpa = ""
        self.courses = []

    def display_student(self):
        print("StuID:", self.sid)
        print("Student Name:", self.stuname)
        for x in self.courses:
            print("Course Registered:", x.coursename)

    def add_student(self):
        self.sid = input("Enter the student ID: ")
        self.stuname = input("Enter the student name: ")

    def register_course(self, cc1):
        self.courses.append(cc1)


class Course:
    def __init__(self):
        self.cid = ""
        self.coursename = ""

    def add_course(self):
        self.cid = input("Enter the course ID: ")
        self.coursename = input("Enter the course name: ")


s1 = Student()
cc1 = Course()
cc2 = Course()

s1.add_student()
s1.display_student()

cc1.add_course()
cc2.add_course()
s1.register_course(cc1)
s1.display_student()
s1.register_course(cc2)
s1.display_student()

quit()