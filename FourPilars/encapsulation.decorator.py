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

    # def get_age(self):
    #     """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
    #     return self.__age

    @property
    def age(self):
        return self._age

    # def set_age(self, value):
    #     """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
    #     if value < 0: 
    #         print('나이는 0 보다 작을 수 없습니다. 기본 값 0 으로 설정하겠습니다')
    #         self.__age = 0
    #     else: 
    #         self.__age = value 

    @age.setter
    def age(self, value):
        if value < 0: 
            print('나이는 0 보다 작을 수 없습니다. 기본 값 0 으로 설정하겠습니다')
            self._age = 0
        else: 
            self._age = value 


young = Citizen('Ana Lee', '26', '123456789')
print(young.age) #26  이때는 같은 이름을 가진 age 메소드를 실행하 
young.age = 30 #이때는 setter method인 age method 가 자동 실행된다 ; age 라는 setter method 를 실행하라
# value 파라미터로 30 전달된다. 
print(young.age) #30


"""
이제 citizen class 에는 _age 라는 인스턴스 변수가 있는거고 age 는 _age에 대한 getter, setter 메소드의 이름이다


property 데코레이터 함수를 적용하면 마치 age 라는 변수가 있는 것 처럼 
age의 값을 읽을 때 age라는 getter 메소드가 실행되고, age의 값을 설정할 때는 age라는 setter 메소드가 실행된다.
when _age is the instance.
"""