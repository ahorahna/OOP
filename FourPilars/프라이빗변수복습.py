import math 
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

#  getter, setter 선언
    
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양수여야 합니다")
        self.__radius = value



circle = Circle(10)
print("# 원의 둘레와 넓이를 구한다.")
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())
print()
# print(circle.__radius)
# print(circle.radius())

### problème 1 
### problème 2 -in vehicles why not using self._speed in start and __str__ method?

circle.radius = 2
print("변경된 원의 반지름: ", circle.radius)

print("강제로 예외를 발생시커 봅니다")
circle.radius = -10