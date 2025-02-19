"""
Create a class "BankAccount" with attributes account number and balance. Implement
methods to deposit and withdraw funds, and a display method to show the account details.
"""

class BankAccount:
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

    def display(self):
        print(f"Account No: {self.acc_no}, Balance: {self.balance}")

def bankaccount_menu():
    acc_no = input("Enter Account Number: ")
    account = BankAccount(acc_no)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Display Account")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

bankaccount_menu()
