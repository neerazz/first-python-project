class Accounts:

    def _init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        if amount < 0:
            print("Deposit Amount should be positive.")
        else:
            self.balance += amount
            print(f"Deposit accepted. New Balance: {self.balance}")

    def withdraw(self, amount: int):
        if self.balance < amount:
            print(f"Withdraw exceeded the available balance.")
        elif amount < 0:
            print("Withdraw amount should be positive.")
        else:
            self.balance -= amount
            print(f"Withdrawal accepted. New Balance: {self.balance}")

    def __str__(self):
        return f"Account Name    : {self.owner}\nAccount Balance : {self.balance}"
