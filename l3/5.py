class Account:
    def __init__(self):
        self.owner = input()  
        self.balance = float(input())  

    def deposit(self):
        amount = float(input())  
        self.balance += amount  

    def withdraw(self):
        amount = float(input())  
        if amount > self.balance:
            print("Insufficient balance!")  
        else:
            self.balance -= amount  

    def show_balance(self):
        print(f"Account owner: {self.owner}, Current balance: {self.balance}")


account = Account()


account.deposit()
account.show_balance()

account.withdraw()
account.show_balance()
