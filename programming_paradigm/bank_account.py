class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize a BankAccount instance with an initial balance."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account if sufficient balance exists."""
        if amount > self.__account_balance:
            return False
        elif amount > 0:
            self.__account_balance -= amount
            return True
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
