class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        else:
            print("Error: Deposit amount must be positive.")
            return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        else:
            print("Insufficient funds")
            return self._balance

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"Account {self.account_number} - Owner: {self.owner} - Balance: ${self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance, interest_rate):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

    def withdraw(self, amount):
        if self._balance - amount < 100:
            print("Cannot go below $100 minimum")
            return self._balance
        else:
            return super().withdraw(amount)
