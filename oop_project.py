from bank_accounts import *

Arion = BankAccount(1000, "Arion")
Riona = BankAccount(2000, "Riona")

Arion.getBalance()
Riona.getBalance()

Riona.deposit(500)

Arion.withdraw(10000)
Arion.withdraw(10)

Arion.transfer(10000, Riona)
Arion.transfer(100, Riona)

Rabin = InterestRewardsAcct(1000, "Rabin")

Rabin.getBalance()
Rabin.deposit(100)
Rabin.transfer(100, Arion)

Rina = SavingsAcct(1000, "Rina")
Rina.getBalance()
Rina.deposit(100)
Rina.transfer(1000, Riona)
