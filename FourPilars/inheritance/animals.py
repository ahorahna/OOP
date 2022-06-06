class Dog:
    def __init__(self, speed_value): 
        self.speed = speed_value

    def run(self):
        print("a dog is running on {}km/h speed".format(self.speed))

class Cat:
    def __init__(self, speed_value): #parameter 이름이 같아도 되네 
        self.speed = speed_value 

    def run(self):
        print("a cat is running on {}km/h speed".format(self.speed))

dog = Dog(30)
cat = Cat(20)

zoo = []
zoo.append(dog)
zoo.append(cat)

for animals in zoo: 
    animals.run()