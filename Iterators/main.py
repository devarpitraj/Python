tup = ('A', 'B', 'C')
myitr = iter(tup)

print(myitr)
print(next(myitr))
print(next(myitr))
print(next(myitr))

str = 'banana'
myitr = iter(str)

print(next(myitr))
print(next(myitr))
print(next(myitr))

# create a iterator class

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a <<= 1
        return x
    
obj = Mynumbers()
myitr = iter(obj)

print(myitr)
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))
print(next(myitr))

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 50:
            x = self.a
            self.a <<= 1
            return x
        else:
            raise StopIteration
        
obj = Mynumbers()
myitr = iter(obj)

for x in myitr:
    print(x)    