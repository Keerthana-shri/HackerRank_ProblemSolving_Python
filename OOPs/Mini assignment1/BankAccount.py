class BalanceException(Exception):
    pass

class BankAccountClass:
    def __init__(self, InitialAmount, AccountName):
        self.balance= InitialAmount
        self.name= AccountName
        print(f"\nAccount '{self.name}' is created. \nBalance = Rs. '{self.balance:.2f}'")
    
    def GetBalance(self):
        print(f"\nAccount Recipient Name:{self.name} \nBalance: Rs. {self.balance:.2f}")
    
    def Deposit(self, amount):
        self.balance= self.balance + amount
        print("\nDeposit Added.")
        self.GetBalance()
    
    def ViableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(f"\nHi {self.name}, your account has insufficient balance of Rs. {self.balance:.2f}")
        
    def Withdraw(self,amount):
        try:
            self.ViableTransaction(amount)
            self.balance= self.balance - amount
            print("\nWithdraw Complete.")
            self.GetBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def Transfer(self, amount, account):
        try:
            print ("\nBeginning Transaction.....")
            self.ViableTransaction(amount)
            self.Withdraw(amount)
            account.Deposit(amount)
            print("\nTransfer Complete✔️✔️✔️")
        except BalanceException as error:
            print(f"\nTransfer Interrupted {error}")
    
class InterestRewardsAccount(BankAccountClass): 
    def Deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.GetBalance()

class SavingsAccount(InterestRewardsAccount):
    def __init__(self, InitialAmount, AccountName): 
        super().__init__(InitialAmount, AccountName)
        self.fee = 5

    def Withdraw(self, amount): 
        try: 
            self.ViableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.GetBalance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')
        

