class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount): #파라미터가 추가됨. 잘못 오버라이딩 한 것: 즉 raise_pay 메소드는 self 외에는 파라미터를 받지 않는다는 규약을 어김  
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다" #return 값 int into string 잘못 오버라이딩 한 것 


employee1 = Employee('김나나', 9000)
employee2 = Employee('고주몽', 8000)

cashier = Cashier('최공공', 13000)

employee_list = []
employee_list.append(employee1)
employee_list.append(employee2)
employee_list.append(cashier) 

for employee in  employee_list:
    employee.raise_pay()
    print(employee.wage)

total_wage = 0

for employee in  employee_list:
    total_wage += employee.wage

print(total_wage)