from math import pi, sqrt #원주율,
from abc import ABC, abstractmethod #추상화기초클라스

#추상 메소드: 자식 클라스가 반드시 오버라이딩 해야 되는 메소드 
# 이런 추상 메소드가 하나 이상 있어야 추상클라스가 된다. 
# 그러니까 추상클라스는 1) ABC 를 상속받고 2)적어도 하나 이상의 추상메소드를 가져야 한다.

class Shape(ABC):
    """도형 클라스"""
    @abstractmethod 
    def area(self) -> float: #type hinting 을 쓰면 자식클라스에서 이 메소드를 어떻게 오버라이딩 해줘야 되는지 감도 준다.
        """도형의 넓이를 리턴한다: 자식 클라스가 오버라이딩 할 것"""
        pass 

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클라스가 오버라이딩 할 것"""
        pass 

class EquilateralTriangle(Shape):
    """정삼각형 클라스
    일반 상속의 문제점: isinstance(shape, Shape)는 True 가 되겠지만, NoneTypeError가 뜸: area , perimeter
    메소드를 오버라이딩 하지 않음!!!"""
    def __init__(self, side):
        self.side = side 

# area, perimeter를 오버라이딩 하지 않음: 그럼 이것도 그대로 abstract class 로 남음

class Rectangle(Shape): 
    """직사각형 클라스"""
    def __init__(self , width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def  perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return (2*self.width) + (2*self.height)

    def __str__(self):
        """직사각형 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이{}인 직사각형".format(self.width, self.height)

class Circle(Shape): 
    """원 클라스"""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def  perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원 정보를 문자열로 리턴한다"""
        return "반지름{}인 직사각형".format(self.radius)

class Cylinder: 
    """원통 클라스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴한다"""
        return "밑변 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)

class Paint:
    """ 그림판 프로그램 클라스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print('넓이, 둘레를 구하는 메소드가 없는 도형을 추가할 수 없습니다!')

        """그림판에 도형을 추가한다"""
    
    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes]) 
                                                           
    def total_perimeter_of_shapes(self):
        """그림팡네 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들: \n\n"
        for shape in self.shapes:
            res_str += str(shape) + '\n'
        return res_str


shape = Shape()
cylinder = Cylinder(7, 4)
rectangle = Rectangle(3, 7)
circle = Circle(4)

paint_program = Paint()
paint_program.add_shape(cylinder)
paint_program.add_shape(circle)
paint_program.add_shape(rectangle)

print(paint_program.total_perimeter_of_shapes())
print(paint_program.total_area_of_shapes())










