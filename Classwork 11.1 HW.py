#Define a class Book(BookID, BookName, Title, Author)
#Define a class User(userID, userName, BooksBorrowed=[])

#Create 5 book objects

#Create 2 user objects
#Add books to the users

class Book:
    def __init__(self):
        self.bid = ""
        self.bcat = ""
        self.title = ""
        self.author = ""

    def add_book(self):
        self.bid = input("Enter the book ID: ")
        self.bcat = input("Enter the book category: ")
        self.title = input("Enter the book title: ")
        self.author = input("Enter the book author: ")

class User:
    def __init__(self):
        self.uid = ""
        self.uname = ""
        self.books = []

    def add_user(self):
        self.uid = input("Enter the user ID: ")
        self.uname = input("Enter the users's name: ")

    def display_user(self):
        print("User name:", self.uname)
        for x in self.books:
            print("Books checked out:", x.title)

    def check_book(self, b):
        self.books.append(b)

u1 = User()
u2 = User()
b1 = Book()
b2 = Book()
b3 = Book()
b4 = Book()
b5 = Book()

b1.add_book()
b2.add_book()
b3.add_book()
b4.add_book()
b5.add_book()

u1.add_user()
u2.add_user()

u1.check_book(b1)
u1.check_book(b2)
u1.check_book(b3)
u2.check_book(b4)
u2.check_book(b5)

u1.display_user()
u2.display_user()