class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

u1 = User("steven", 5000)
u2 = User("Caleb", 9000)
u3 = User("Dan", 2000)
u1.display_user_balance().make_deposit(300).make_deposit(50).make_deposit(50).make_withdrawal(250).display_user_balance()
u2.make_deposit(500).make_deposit(600).make_withdrawal(50).make_withdrawal(500).display_user_balance()
u3.make_deposit(50).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()
u1.transfer_money(u3, 50).display_user_balance()
u3.display_user_balance()
