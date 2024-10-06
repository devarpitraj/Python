class Myclass:
    x = 5
    
print(Myclass)

obj = Myclass() # object
print(obj.x)

class Person:
    def __init__(self, name, age):  # automatically called everytime when obj is created
        self.name = name
        self.age = age
        
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # def __str__(self):
    #     return f"{self.name}({self.age})"
    
p1 = Person("John", 36)
print(p1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myfunc(self):
        print("Hello, " + self.name)
        
p1 = Person("John", 36)
p1.myfunc()

# any name can be used instead of self
class Person:
    def __init__(myobj, name, age):
        myobj.name = name
        myobj.age = age
        
    def __str__(var):
        return f"{var.name}({var.age})"
    
p1 = Person("John", 36)
print(p1)

# modify obj property
p1.age = 48
print(p1.age)

# delete obj property
del p1.age
# print(p1.age)   # Error

# delete object
del p1

# pass statement
class Person:
    pass
