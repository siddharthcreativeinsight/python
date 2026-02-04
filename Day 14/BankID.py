#creating a bank Account
class BankAccount:
    def __init__(self, name, balance=20000):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposited. new balance is {self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"{amount} withdraw. new balance is {self.balance}")
        else:
            print(f"{amount} not deposited. new balance is {self.balance}")

    def display(self):
        print(f"Account Holder:{self.name}")
        print(f"Balance:{self.balance}")


account = BankAccount("sidd")
account.deposit(50)
account.withdraw(45000)
account.display()
