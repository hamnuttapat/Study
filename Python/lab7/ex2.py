
class BankAccount:
    def __init__ (self, bank, owner, acc_numeber, total):
        self.bank = bank
        self.owner = owner
        self.acc_number = acc_numeber
        self.total = total
    def balance_error(self, balances):
        if balances < 0:
            print("Wrong balance")
        else:
            self.total = self.total + balances
    def depo_error(self, depos):
        if depos < 0:
            print("Wrong deposit")
        else:
            self.total = self.total + depos
    def withdraw_error(self, withdraws):
        if withdraws < 0:
            print("Wrong withdraw")
        elif self.total < withdraws:
            print("Wrong withdraw")
        else:
            self.total = self.total - withdraws
    def print(self):
        print(self.total)



properties = BankAccount("Bangkok bank", "Nuttapat Wuttiutadom", "12345", 0)
properties.balance_error(1000)
properties.depo_error(20)
properties.withdraw_error(50) 
properties.print()