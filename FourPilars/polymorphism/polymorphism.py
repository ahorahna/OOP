# import Math 
# pi = 
from math import pi 

class Rectangle: 
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


class Circle: 
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

    # def add_shape(self, shape):
    #     """그림판에 도형을 추가한다"""
    #     self.shapes.append(shape)

    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        # isinstance method 
        if isinstance(shape, Circle) or isinstance(shape, Rectangle):
            self.shapes.append(shape)
        else:
            print('넓이, 둘레를 구하는 메소드가 없는 도형을 추가할 수 없습니다!')
    
    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes]) # 리스트 컴프리헨션 
                                                            # sum은 배열안의 수를 모두 더한 값을 리턴
                                                            # shape.area() - 이상하게 느껴짐: polymorphism
        
    def total_perimeter_of_shapes(self):
        """그림팡네 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들: \n\n"
        for shape in self.shapes:
            res_str += str(shape) + '\n'
        return res_str




paint_program = Paint()
cylinder = Cylinder(7, 4)
rectangle = Rectangle(3, 7)
circle = Circle(4)


paint_program.add_shape(cylinder)
paint_program.add_shape(circle)
paint_program.add_shape(rectangle)

print(paint_program.total_perimeter_of_shapes())
# 에러가 난다! -> 그래서 ininstance method 를 썼다 (거르기 위해서)
# 상속없는 다양성의 한계
print(paint_program.total_area_of_shapes())



