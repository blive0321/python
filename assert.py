# assert 斷言的用法，斷言在如果expression不滿足的情況下會直接return錯誤

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
# Balance :  1000

# a.deposit(-500)
# AssertionError: 必須是大於 0 的整數

# a.withdraw(2000)
# RuntimeError: balance not enough
