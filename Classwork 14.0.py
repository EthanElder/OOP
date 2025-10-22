class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.email = ""
        self.Balance = 0.00

    def add_customer(self):
        self.cid = input("Enter the new customer ID: ")
        self.acc_no = input("Enter the account number: ")
        self.cname = input("Enter the customer name: ")
        self.phone = input("Enter the customer phone number: ")
        self.email = input("Enter the customer email: ")
        self.Balance = float(input("Enter the starting balance: "))

    def debit_from(self):
        self.Balance -= float(input("Enter the amount of debit taken: "))

    def credit_to(self):
        self.Balance += float(input("Enter the amount of credit earned: "))

    def display_all(self):
        print("Customer ID:", self.cid)
        print("Account number:", self.acc_no)
        print("Name:", self.cname)
        print("Phone #:", self.phone)
        print("Email:", self.email)
        print("Balance:", self.Balance)

#Main Code

c1 = Customer()
c2 = Customer()

c1.add_customer()
c2.add_customer()

c1.debit_from()
c2.credit_to()

c1.display_all()
c2.display_all()