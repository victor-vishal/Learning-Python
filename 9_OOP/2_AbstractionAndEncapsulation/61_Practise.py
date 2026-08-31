# Create account class with 2 attributes: account_number and balance. The balance attribute should be private. Implement methods to deposit, withdraw, and check the balance.
# create methods for debit, credit and checking balance.


class Account:

    def __init__(self, bal, accnum):
        self.balance = bal
        self.account_number = accnum
        print(f"Account created with account number: {self.account_number} and balance: {self.balance}")

    def debit(self, amount):
        self.balance -= amount
        print(f"Debited {amount} from your account")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount} to your account")

    def check_balance(self):
        print(f"Your account balance is: {self.balance}")

act1 = Account(1000, 123456)
act1.debit(500)
act1.check_balance()