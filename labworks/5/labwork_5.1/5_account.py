class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Insufficient balance")

    def display(self):
        print("Balance:", self.__balance)


a1 = Account()

a1.deposit(5000)
a1.withdraw(1000)
a1.display()