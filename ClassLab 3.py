class Author:
    def __init__(self):
        self.aid = ""
        self.aname = ""
        self.affiliation = ""
        self.county = ""
        self.phone = ""
        self.email = ""

    def add_author(self):
        self.aid = input("Enter the author ID: ")
        self.aname = input("Enter the author's name: ")
        self.affiliation = input("Enter the author's affiliation: ")
        self.county = input("Enter the author's country: ")
        self.phone = input("Enter the author's phone number: ")
        self.email = input("Enter the author's email address: ")

class Book:
    def __init__(self):
        self.bid = ""
        self.title = ""
        self.author = []
        self.publisher = ""
        self.yr_publish = ""

    def add_book(self):
        self.bid = input("Enter the book ID: ")
        self.title = input("Enter the book title: ")
        self.publisher = input("Enter the book publisher: ")
        self.yr_publish = input("Enter the year the book was published: ")

    def display_book(self):
        print("Book ID:", self.bid)
        print("Title:", self.title)
        for x in self.author:
            print("Author:", x.aname)

    def assign_author(self, a):
        self.author.append(a)

class User:
    def __init__(self):
        self.uid = ""
        self.uname = ""
        self.pword = ""
        self.address = ""
        self.phone = ""
        self.email = ""
        self.books = []

    def add_user(self):
        self.uid = input("Enter the user ID: ")
        self.uname = input("Enter the user's name: ")
        self.pword = input("Enter the password: ")
        self.address = input("Enter the user's home address: ")
        self.phone = input("Enter the user's phone number: ")
        self.email = input("Enter the user's email address: ")

    def display_user(self):
        print("User ID:", self.uid)
        print("User name:", self.uname)
        for x in self.books:
            print("Books checked out:", x.title)

    def check_book(self, b):
        self.books.append(b)


u1 = User()
u2 = User()
u3 = User()
a1 = Author()
a2 = Author()
a3 = Author()
b1 = Book()
b2 = Book()
b3 = Book()

u1.add_user()
b1.add_book()
a1.add_author()
b1.assign_author(a1)
u1.check_book(b1)
u1.display_user()
b1.display_book()

u2.add_user()
b2.add_book()
a2.add_author()
b2.assign_author(a2)
u2.check_book(b2)
u2.display_user()
b2.display_book()

u3.add_user()
b3.add_book()
a3.add_author()
b3.assign_author(a3)
u3.check_book(b3)
u3.display_user()
b3.display_book()