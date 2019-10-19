class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print('Deposit Successful!')
        return self.balance
    def withdraw(self,amount):
        if amount >  self.balance:
            return RuntimeError('The amount requested exceeded available balance.')
        self.balance -= amount
        return self.balance
acct1 = Account('Jose', 100)      
acct1.owner