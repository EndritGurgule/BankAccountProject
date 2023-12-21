from bank import *

Ardi = BankAccount(1000, "Ardi")
Faruk = BankAccount(2000, "Faruk")

Ardi.getBalance()
Faruk.getBalance()

Faruk.deposit(500)

Ardi.withdraw(10000)
Ardi.withdraw(10)
              
Ardi.transfer(10000, Faruk)
Ardi.transfer(100, Faruk)

Endrit = InterestRewardsAcct(1000, "Endrit")

Endrit.getBalance()

Endrit.deposit(100)

Endrit.transfer(100, Ardi)

Ali = SavingsAcct(1000, "Ali")

Ali.getBalance()

Ali.deposit(100)
Ali.transfer(1000, Faruk)