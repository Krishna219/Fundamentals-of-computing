class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.penality = 5
        self.fees = 0
        """Creates an account with the given balance."""
    
    def __str__(self):
        return "Balance : " + str(self.balance) + " | Withdrawal fees : " + str(self.fees)     
       
    
    def deposit(self, amount):
        self.balance += amount
        """Deposits the amount into the account."""
        
    def withdraw(self, amount):
        
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= (amount + 5)
            self.fees += 5            
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
    def get_withdrawals(self):
        return self.withdrawals    
    def get_balance(self):
        return self.balance
        """Returns the current balance in the account."""
        
    def get_fees(self):
        return self.fees
        """Returns the total fees ever deducted from the account."""
        
# practice test case
print "-------------- Practice test case -------------"
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()

# actual test case
print "-------------- Actual test case -------------"
account1 = BankAccount(20)
account1.deposit(10)
account2 = BankAccount(10)
account2.deposit(10)
account2.withdraw(50)
account1.withdraw(15)
account1.withdraw(10)
account2.deposit(30)
account2.withdraw(15)
account1.deposit(5)
account1.withdraw(10)
account2.withdraw(10)
account2.deposit(25)
account2.withdraw(15)
account1.deposit(10)
account1.withdraw(50)
account2.deposit(25)
account2.deposit(25)
account1.deposit(30)
account2.deposit(10)
account1.withdraw(15)
account2.withdraw(10)
account1.withdraw(10)
account2.deposit(15)
account2.deposit(10)
account2.withdraw(15)
account1.deposit(15)
account1.withdraw(20)
account2.withdraw(10)
account2.deposit(5)
account2.withdraw(10)
account1.deposit(10)
account1.deposit(20)
account2.withdraw(10)
account2.deposit(5)
account1.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account2.deposit(10)
account2.deposit(15)
account2.deposit(20)
account1.withdraw(15)
account2.deposit(10)
account1.deposit(25)
account1.deposit(15)
account1.deposit(10)
account1.withdraw(10)
account1.deposit(10)
account2.deposit(20)
account2.withdraw(15)
account1.withdraw(20)
account1.deposit(5)
account1.deposit(10)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()