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
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage) 
        self.numer_sold = number_sold

    def take_order(self, money_received):
        """ 주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print('돈이 충분하지 않습니다')
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + '게산대 직원: ' + self.name 

class DeliveryMan(Employee):

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver_to(self, address): 
        """배달원이 대기 중이면 주어진 주소로 배달을 나갑니다"""
        if self.on_standby:
            print(address + '(으) 로 배달이 나갑니다!') 
            self.on_standby = False # False로 상태 바꿔주기 
        else: 
            print('이미 배달하러 나갔습니다')

    def back(self): 
        """배달원을 복귀 처리한다 """ 
        self.on_standby = True 

    def __str__(self):
        return DeliveryMan.company_name  + '배달원: ' + self.name


class CashierDeliveryMan(DeliveryMan, Cashier):
    def __init__(self, name, wage, on_standby, number_sold=0):
        Employee.__init__(self, name, wage)
        self.on_standby = on_standby
        self.number_sold = number_sold


cashir_and_deliver = CashierDeliveryMan('yoon', 7000, True, 10 )
cashir_and_deliver.take_order(60000)
cashir_and_deliver.deliver_to('관악로 110')

cashir_and_deliver.back()
print(cashir_and_deliver) # kings burger배달원: yoon


print(CashierDeliveryMan.mro())
