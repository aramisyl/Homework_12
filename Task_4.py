class BankAccount:
    def __init__(self, number, balance, owner):
        self.number = number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"Not enough money on account.")
    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
        else:
            print(f"Not enough money on account.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.accounts = []

    def get_total_balance(self):
        total_balance = 0
        for account in self.accounts:
            total_balance += account.balance
        return total_balance