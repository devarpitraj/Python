print(10 > 9)
print(10 < 9)
print('\n')

print(bool("Hello"))
print(bool(""))
print(bool(" "))
print('\n')

print(bool(["apple", "banana"]))
print(bool([]))
print(bool(("A", "B")))
print(bool(()))
print(bool({}))
print('\n')

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))
print('\n')

x = "Hello"
print(isinstance(x, int))
print(isinstance(x, str))
print('\n')