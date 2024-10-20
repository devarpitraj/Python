class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print("Hello, " + self.fname + " " + self.lname)
        
x = Person('Mike', 'Olsen')
x.printname()

class Student(Person):
    pass

x = Student('Mike', 'Olsen')
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)  # self parameter is not passed here
        self.graduateyear = year
        
    def printdetail(self):
        super().printname()
        print(f"Year : {self.graduateyear}")
        
x = Student('Mike', 'Olsen', 2020)
x.printdetail()