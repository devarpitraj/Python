# Class Ploymorphism

class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        print('Move')
        
class Boat:
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        print('Sail')
        
class Plane:
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        print('Fly')
        
car1 = Car("A")
boat1 = Boat("B")
plane1 = Plane("C")

for x in (car1, boat1, plane1):
    x.move()
    
# Inheritance Polymorphism

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def move(self):
        print("Move")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail")
        
class Plane(Vehicle):
    def move(self):
        print("Fly")
        
car1 = Car("A")
boat1 = Boat('B')
plane = Plane('c')

for x in (car1, boat1, plane1):
    x.move()