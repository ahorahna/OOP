class Cashier:
    """계산대 직원 클라스"""
    company_name = '코드잇 버거'
    raise_percentage = 5.05
    burger_price = 7000

    def __init__(self, name, wage, number_sold=0):
        self.name = name
        self.wage = wage
        self.number_sold = number_sold

    def raise_pay(self): 
        """시급을 인상한다"""
        self.wage += self.raise_percentage #Cashier.raise_percentage

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

jiwoong = Cashier('jiwoong choi', 10000, 0)
"""
시급인상 
객체 하나 만든 다음에 ->
instnace method를 쓰는 방법, 
instance variable 인스턴스 변수/ 속성을 프린트 하는 방법
"""

# 임금을 인상시키고, 임금 확인 
jiwoong.raise_pay() #I thought it'd be print(jiwoong.raise_pay()) though I didn't even think of .method()
print(jiwoong.wage) 

# 햄버거 주문 받기 
print(jiwoong.take_order(170000))
print(jiwoong.take_order(5000))

# jiwoong 의 하루 판매량 
print(jiwoong.number_sold)

# instane itself 보기 :__str__ 이용
print(jiwoong)