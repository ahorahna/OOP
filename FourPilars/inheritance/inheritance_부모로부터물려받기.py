## 상속 I. 부모로부터 물려받기
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
    pass


henrik = Cashier('Henrik Do', 8900)
henrik.raise_pay()
print(henrik.wage)
print(henrik)
"""
클라스 정보를 자세히 출력해주는 help 함수! """
# help(Cashier)
print(Cashier.mro())
print(isinstance(henrik, Employee))