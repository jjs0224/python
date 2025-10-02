class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def pay(self):
        print('....')

class CreditCardPayment(Payment):
    def __init__(self, amount, number): #부모클라스 amount 직접여기서도 값넣어줌
        super().__init__(amount) 
        self.number = number

    def pay(self):
        
        print(f'신용카드 번호: {self.number}로 {self.amount} 결제되었습니다')
    
class CashPayment(Payment):
    #def __init__ 여기서 선언안해주면 무조건 parent class __init__ 을사용함

    def pay(self): 
        print(f'{self.amount}원 현금 결제되었습니다.')

c1 = CreditCardPayment(1000,'123-123-123') #신용카드 번호: 123-123-123로 1000 결제되었습니다
c1.pay()

c2 = CashPayment(5000) #부모 __init__ 이 진행되기때문에 amount 를 지정해줘야함
c2.pay() #5000원 현금 결제되었습니다.
