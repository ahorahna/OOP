class BankAccount:
    interest: float = 0.02

    def __init__(self, owner_name: str, balance: float):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance < amount:
            print('insufficient balance')
        else: 
            self.balance -= amount

    def add_interest(self):
        self.balance *= 1 + BankAccount.interest

my_account = BankAccount('Ana Lee', 10000000000000000000000)
#  바로위에 이거 들여쓰기 해서 돌리니까 안돌아감!
my_account.add_interest()
print(my_account.balance)