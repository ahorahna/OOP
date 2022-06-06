from abc import ABC, abstractmethod
from re import A 

# 추상 클라스
class Animal(ABC): 
    
    @abstractmethod
    def run(self):
        pass 

class Dog(Animal):
    def __init__(self, speed_value):
        self.speed = speed_value

    def run(self):
        print("강아지가 {}km/h의 속도로 달립니다.".format(self.speed))


class Cat(Animal):
    def __init__(self, speed_value):
        self.speed = speed_value

    def run(self):
        print("고양이가 {}km/h의 속도로 달립니다.".format(self.speed))

dog = Dog(40)
cat = Cat(15)

zoo = [] 

if isinstance(dog, Animal):
    zoo.append(dog)

if isinstance(cat, Animal):
    zoo.append(cat)


for animals in zoo: 
    animals.run()