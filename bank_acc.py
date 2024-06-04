# Create a class named BankAccount with attributes account_number, holder_name, and balance
# Implement methods deposit and withdraw to modify the balance accordingly
# Ensure that the withdraw method checks if the withdrawal amount is <= to the balance before deducting.
# Instantiate an object of this class, deposit 1000, withdraw 500, and print the final balance.

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, new balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, new balance: {self.balance}")
        else:
            print("Insufficient balance")

# Instantiate an object of the BankAccount class
account = BankAccount("123456789", "John Doe")

# Deposit 1000
account.deposit(1000)

# Withdraw 500
account.withdraw(500)

# Print the final balance
print(f"Final balance: {account.balance}")