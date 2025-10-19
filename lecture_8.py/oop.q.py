class Account:
    def __init__(self,acc,bal):
        self.accounts_no = acc
        self.balance = bal
    
    def debit(self , amount):
        self.balance -= amount
        print("Rs.",amount,"was Debited")

    def credit(self , amount):
        self.balance += amount
        print("Rs.",amount,"was credit")

    def get_balance(self):
        return self.balance



acc1 = Account(10000 , 145723)
acc1.debit(1000)
acc1.credit(500)