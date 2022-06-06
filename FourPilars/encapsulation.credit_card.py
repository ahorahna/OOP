class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit
        
        # 코드를 쓰세요

    # 코드를 쓰세요
    def get_name():
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
    def get_password():
        return "비밀 번호는 볼 수 없습니다."
    
    def set_password(self, value):
        self.__password = value
    
    
    def get_payment_list():
        return self.__payment_list
    
    def set_payment_list(self, value):
        if value < 0 or value >  MAX_PAYMENT_LIMIT:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")
        else:
            return self.__payment_limit = value
    

"""
저 위 가 내가 만든 코드고 모범답안은 아래에 

1) getter 든 setter 든 모두 'self'를 가져야함 ?????
2) return 하는 건 getter methods 에만 쓰임 


"""

class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit
        
        # 코드를 쓰세요

    # 코드를 쓰세요
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
        
    def get_password(self):
        return "비밀 번호는 볼 수 없습니다."
    
    def set_password(self, new_password):
        self.__password = new_password
    
    def get_payment_limit(self):
        return self.__payment_limit
    
    def set_payment_limit(self, new_payment):
        if new_payment < 0 or new_payment > MAX_PAYMENT_LIMIT:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")
        else:
            self.__payment_limit = new_payment

    # 이건 모범답안  
    def set_payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")
    

card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

