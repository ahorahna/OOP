## 상속 II OVERRIDING

class Employee:
    company_name = 'kings burger'
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self.wage = wage

    def raise_pay(self):
        self.wage += self.raise_percentage 

    def __str__(self):
        return Employee.company_name +  "직원: " + self.name 
    
class Cashier(Employee): 
    raise_percentage = 1.05

    """oveerriding 1"""
    def __init__(self, name, wage, number_sold):
        self.name = name
        self.wage = wage
        self.numer_sold = number_sold 

    """oveerriding 2"""
    def __init__(self, name, wage, number_sold):
        Employee.__init__(self, name, wage) #super 도 그렇고 여기 끝에 : 콜론 없음
        self.numer_sold = number_sold

    """ overriding 3:super() 함수 쓰기 - self no needed """
    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)  # self 를 없앰
        self.numer_sold = number_sold

    def __str__(self):
        return Cashier.company_name + "계산대 직원: " + self.name
    