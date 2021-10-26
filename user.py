class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print("User:" , self.name , ", Balance:" , self.account_balance)


blair = User("Blair", "blairyoung009@gmail.com")
bob = User("Bob", "bobyoung009@gmail.com")
bill = User("Bill", "billyoung009@gmail.com")

#print(blair.name)
#blair.display_user_balance()

#user 1
blair.make_deposit(100)
blair.make_deposit(200)
blair.make_deposit(300)
blair.make_withdrawal(500)
blair.display_user_balance()

#user2
bob.make_deposit(400)
bob.make_deposit(600)
bob.make_withdrawal(500)
bob.make_withdrawal(200)
bob.display_user_balance()

#user3
bill.make_deposit(10000)
bill.make_withdrawal(200)
bill.make_withdrawal(300)
bill.display_user_balance()