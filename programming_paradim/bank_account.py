class BankAccount():
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance < amount:
            return self.account_balance - amount
        return "Insuffiient acount balance"

    def display_balance(self):
        print(f'Account Balance Available {self.account_balance}')
