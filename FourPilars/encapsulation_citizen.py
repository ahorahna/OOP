class Citizen: 
    """주민 클라스"""
    drink_age = 19
    
    def __init__(self, name, age, residnet_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        # self.__age = age
        self.set_age(age)
        self.__resident_id = residnet_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drink_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + self.__age + "살 입니다."
    #getter method 
    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self.__age
    #setter method 
    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0: 
            print('나이는 0 보다 작을 수 없습니다. 기본 값 0 으로 설정하겠습니다')
            self.__age = 0
        else: 
            self.__age = value 
        

young = Citizen('young kim', -19, '9683038')
print(young.get_age())

young.set_age(-10)
print(young.get_age())

young.set_age(20)
print(young.get_age())