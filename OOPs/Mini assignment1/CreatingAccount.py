from BankAccount import *

Keerthana = BankAccountClass(1500, "Keerthana")
Shri = BankAccountClass(3000, "Shri")

Keerthana.GetBalance()
Shri.GetBalance()

Shri.Deposit(6000)

Keerthana.Withdraw(100)
Keerthana.Withdraw(2000)

Shri.Transfer(4000, Keerthana) 

Katara = InterestRewardsAccount(1000, "Katara")

Katara.GetBalance()

Katara.Deposit(1000)

Katara.Transfer(1000, Keerthana)

Arisu = SavingsAccount(1000, "Arisu")

Arisu.GetBalance()

Arisu.Deposit(100)

Arisu.Transfer(10000, Shri)
Arisu.Transfer(1000, Shri)