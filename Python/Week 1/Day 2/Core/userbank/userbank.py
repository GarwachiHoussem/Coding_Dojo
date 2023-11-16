class BankAccount:
    def __init__(self, int_rate, balance=0.00): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if amount<self.balance:
            self.balance -= amount
        else:
            self.balance -= 5.00
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance: $"+str(self.balance))

    def yield_interest(self):
        if self.balance>0.00:
            self.balance+=self.balance*self.int_rate
        return self
account1 = BankAccount(0.05)
account2 = BankAccount(0.05)

account1.deposit(1000).deposit(500).deposit(2000).withdraw(3000).yield_interest().display_account_info()
account2.deposit(1000).deposit(1000).withdraw(200).withdraw(500).withdraw(500).withdraw(1000).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
    
