class DeliveryMan:
    """배달원 클라스"""
    company_name = '코드잇 버거' 
    raise_percentage = 1.03

    def __init__(self, name, wage, on_standby):
        self.name = name
        self.wage = wage
        self.on_standby = on_standby

    def raise_pay(self):
        """시급을 인상한다 """
        self.wage *= self.raise_percentage

    def deliver(self, address): 
        """배달원이 대기 중이면 주어진 주소로 배달을 나갑니다"""
        if self.on_standby:
            print(address + '(으) 로 배달이 나갑니다!') 
            self.on_standby = False # False로 상태 바꿔주기 
        else: 
            print('이미 배달하러 나갔습니다')

    def back(self): 
        """배달원을 복귀 처리한다 """ 
        # 이걸 자동으로 실행시킬 수 있는 방법이 없나?? following deliver  True method?
        self.on_standby = True 

    def __str__(self):
        return DeliveryMan.company_name  + '배달원: ' + self.name

olie = DeliveryMan('Olivia Lin in London', 7000, True)
# 시급을 인상 해준다
olie.raise_pay()
print(olie.wage) 

olie.deliver('Seoul, GwanakGu, SNU 11 dong ')
olie.deliver('Seoul, GwanakGu, SNU 12 dong ')

olie.back()
olie.deliver('Seoul, GwanakGu, SNU 33 dong ')
print(olie)