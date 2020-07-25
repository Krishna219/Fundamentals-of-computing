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
my_account = BankAccount(10)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(20)
print my_account
print
print my_account.get_balance(), my_account.get_fees()

        
# actual test case
print "-------------- Actual test case -------------"
my_account = BankAccount(10)
print my_account
print 
my_account.withdraw(5)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(5)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(20)
print my_account
print
my_account.withdraw(5)
print my_account
print 
my_account.deposit(10)
print my_account
print
my_account.deposit(20)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(30)
print my_account
print
my_account.withdraw(10)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(50)
print my_account
print 
my_account.deposit(30)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(5)
print my_account
print 
my_account.deposit(20)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.deposit(30)
print my_account
print
my_account.withdraw(25) 
print my_account
print
my_account.withdraw(5)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(10)
print my_account
print 
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.deposit(30)
print my_account
print
my_account.withdraw(25) 
print my_account
print
my_account.withdraw(10)
print my_account
print
my_account.deposit(20)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(5)
print my_account
print 
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(5)
print my_account
print 
my_account.withdraw(15)
print my_account
print
my_account.deposit(10)
print my_account
print
my_account.withdraw(5) 
print my_account
print
print my_account.get_balance(), my_account.get_fees()     
        
#my_account = BankAccount(10)
#my_account.withdraw(5)
#my_account.deposit(10)
#my_account.withdraw(5)
#my_account.withdraw(15)
#my_account.deposit(20)
#my_account.withdraw(5) 
#my_account.deposit(10)
#my_account.deposit(20)
#my_account.withdraw(15)
#my_account.deposit(30)
#my_account.withdraw(10)
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.withdraw(50) 
#my_account.deposit(30)
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.withdraw(5) 
#my_account.deposit(20)
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.deposit(30)
#my_account.withdraw(25) 
#my_account.withdraw(5)
#my_account.deposit(10)
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.withdraw(10) 
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.deposit(30)
#my_account.withdraw(25) 
#my_account.withdraw(10)
#my_account.deposit(20)
#my_account.deposit(10)
#my_account.withdraw(5) 
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.withdraw(5) 
#my_account.withdraw(15)
#my_account.deposit(10)
#my_account.withdraw(5) 
#print my_account.get_balance(), my_account.get_fees()