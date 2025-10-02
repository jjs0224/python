class Wage():
    
    total = 0
    
    def __init__(self, name, hours, hourly_wage):
        self.name = name
        self.hours = hours
        self.hourly_wage = hourly_wage

    def calc_pay(self):
        
        if self.hours <= 40 :
            Wage.total = self.hours*self.hourly_wage
        else:
            Wage.total = (40*self.hourly_wage)+((self.hours - 40) *(self.hourly_wage*1.5))
        
        return f'Pay for {self.name} : ${self.total}'
    
name = input('Enter person name:')
hour = int(input('Enter person hour:'))
wage = int(input('Enter hourly wage'))
ob1 = Wage(name,hour,wage)

print(ob1.calc_pay())
