class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)


class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest Added:", interest)


obj = SavingAccount("Fennie", 10000, 5)

obj.deposit(2000)
obj.withdraw(1000)
obj.add_interest()
obj.show_balance()