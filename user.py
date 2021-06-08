class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def make_deposit(self, amount):
        self.account_balance += amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

u1 = User("steven", 500)
u2 = User("Caleb", 9001)
u3 = User("Dan", 2077)
u1.display_user_balance()
u1.make_deposit(300)
u1.make_deposit(45)
u1.make_deposit(60)
u1.make_withdrawal(250)
u1.display_user_balance()
u2.make_deposit(500)
u2.make_deposit(600)
u2.make_withdrawal(50)
u2.make_withdrawal(500)
u2.display_user_balance()
u3.make_deposit(250)
u3.make_withdrawal(25)
u3.make_withdrawal(45)
u3.make_withdrawal(30)
u3.display_user_balance()
u1.transfer_money(u3, 72)
u1.display_user_balance()
u3.display_user_balance()
