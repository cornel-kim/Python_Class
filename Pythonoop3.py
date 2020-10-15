#Bank account- Deposit, withdraw

class Account:
    def __init__(self, name, accno, age, phone, charges, balance):
        self.name = name
        self.accno = accno
        self.age = age
        self.phone = phone
        self.charges = charges
        self.balance = balance

    def Deposit(self, amount_deposited):
        self.balance = amount_deposited + self.balance
        transaction_fee = 5
        print('Your new balance after deposit is', self.balance - transaction_fee)
        #send a text to user
        print('A notification text has been sent to you', self.phone)

    def Withdraw(self, amount_withdrawn):
        self.balance = self.balance - amount_withdrawn
        print("The amount withdrawn is", amount_withdrawn)
        print("The remaining balance is", self.balance)


x = Account('James', 1234321, 20, +6476598756, 100, 400)
x.Deposit(amount_deposited=1000)
x.Withdraw(amount_withdrawn=500)