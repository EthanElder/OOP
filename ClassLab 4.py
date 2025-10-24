import pickle
class Customer:
    def __init__(self):
        self.cid = ""
        self.acc_no = ""
        self.cname = ""
        self.phone = ""
        self.email = ""
        self.Balance = 0.00
        self.debit_card = ""
        self.credit_card = []

    def add_customer(self):
        self.cid = input("Enter the new customer ID: ")
        self.acc_no = input("Enter the account number: ")
        self.cname = input("Enter the customer name: ")
        self.phone = input("Enter the customer phone number: ")
        self.email = input("Enter the customer email: ")
        self.Balance = float(input("Enter the starting balance: "))
        print("------------------------------------------------")

    def debit_from(self):
        self.Balance -= float(input("Enter the amount of debit taken: "))
        print("------------------------------------------------")

    def credit_to(self):
        self.Balance += float(input("Enter the amount of credit earned: "))
        print("--------------------------------------------------")

    def assign_credit_card(self, card):
        self.credit_card.append(card)

    def assign_debit_card(self):
        self.debit_card = card2

    def display_customer(self):
        print("Customer ID:", self.cid)
        print("Account number:", self.acc_no)
        print("Name:", self.cname)
        print("Phone #:", self.phone)
        print("Email:", self.email)
        print("Balance:", self.Balance)
        print("Credit Card(s):", self.credit_card)
        print("Debit Card:", self.debit_card)
        print("-------------------------------------------------")

class Card:
    def __init__(self):
        self.type = ""
        self.card_no = ""
        self.cvv = ""
        self.exp_date = ""
        self.balance = 0.00

    def add_card(self):
        self.type = input("Enter if you want debit or credit: ")
        self.card_no = input("Enter the card number: ")
        self.cvv = input("Enter the CVV/security number: ")
        self.exp_date = input("Enter the expiration date: ")
        self.balance = float(input("Enter the credit max or debit balance: "))
        print("-----------------------------------------------------")

    def display_card(self):
        print("Type:", self.type)
        print("Card Number:", self.card_no)
        print("CVV:", self.cvv)
        print("Expiration Date:", self.exp_date)
        print("Balance:", self.balance)
        print("------------------------------------------------------")

#Main Code

cust1 = Customer()
cust2 = Customer()

cust1.add_customer()
cust2.add_customer()

card1 = Card()
card2 = Card()

card1.add_card()
card2.add_card()

cust1.debit_from()
cust2.credit_to()

cust2.assign_credit_card(card1)
cust2.assign_debit_card()

cust1.display_customer()
cust2.display_customer()

card1.display_card()
card2.display_card()

f1 = open("bank.dat", "ab")
pickle.dump(cust1, f1)
pickle.dump(cust2, f1)
pickle.dump(card1, f1)
pickle.dump(card2, f1)
f1.close()

quit()