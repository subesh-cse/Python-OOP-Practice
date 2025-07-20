# encapsulation.py
# Demonstrating encapsulation using private variables and getter/setter methods

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance  # getter

# Create account and perform operations
account1 = BankAccount("Subesh", 1000)
account1.deposit(500)
account1.withdraw(300)
print(f"Current balance: ₹{account1.get_balance()}")

# Trying to access private variable directly (won't work)
# print(account1.__balance)  # Uncomment to see error
