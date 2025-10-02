class Calc():
    @staticmethod #classmethod 같이 공용으로 사용가능한데 얘는 parameter로 value 받아서 처리함.. NO CLS
    def add(n1, n2):
        print(n1+n2)

    @staticmethod
    def mul(n1, n2):
        print(n1*n2)

Calc.add(10,20) #30
Calc.mul(10,20) #200