class Account:
    def __init__(self, balance):
        self.balance = balance  

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Funds"
        else:
            self.balance -= amount
            return self.balance

s = input().split()
balance = int(s[0])
withdraw_amount = int(s[1])

acc = Account(balance)

print(acc.withdraw(withdraw_amount))