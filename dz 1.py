#домашнє завдання для "ООП. Класи. Атрибути та методи класів."
class bank_acount:
    def __init__(self, money):
        self.money = money
    def withdraw(self):
        cassh = int(input("how much money to withdraw? "))
        if cassh > self.money:
            print ("not enough green in bank!")
        elif cassh == 0:
            print ("are we serious right now")
        else:
            self.money -= cassh

            print("money on bank acount: " + str(self.money))
    def deposit(self):
        self.money += int(input("how much money to deposit? "))
        print("money on bank acount: " + str(self.money))

    def command(self):
        comand = str(input("what action do you want to do(withdraw or deposit)? "))
        if comand == "withdraw":
            self.withdraw()
        elif comand == "deposit":
            self.deposit()
        else:
            print("incorrect action")

cash = bank_acount(int(input("how much starting money? ")))

for i in range(100):
    cash.command()
#purely human no ai
