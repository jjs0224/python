class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance #__ underbar 2 개 앞에넣어주면 내부에서만 사용가능 =>  makes it private

    def deposit(self, amount):
        self.__balance += amount
        print(f'{amount}원이 입금되었습니다. 현재 잔액:{self.__balance}')

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f'{amount}원이 출금되었습니다. 현재 잔액:{self.__balance}')
        else:
            print(f'잔액 부족')

    def show_balance(self):
        print(f'계좌주: {self.owner}, 현재 잔액: {self.__balance}원')

bac1 = BankAccount('kim', 10000)
bac1.show_balance()

bac1.deposit(2000)
bac1.withdraw(7000)
bac1.show_balance()

print(bac1.__balance) #접근불가능
print(bac1._BankAccount__balance) #하지만클라스 선언하면 접근가능..?