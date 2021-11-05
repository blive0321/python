class Account():
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        assert amount > 0, "必須是大於 0 的整數"
        self.balance += amount

    def withdraw(self, amount):
        assert amount > 0, "必須是大於 0 的整數"
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise RuntimeError("balance not enough")

a = Account("A123" , "Brandon")
a.deposit(1000)
print("Balance : ", a.balance)
