import mymodule

mymodule.greeting("John")
print(mymodule.person1["age"])

import platform as pf

x = pf.system()
print(x)

x = dir(pf) # dir() is used to list all functions in a module
# print(x)

from mymodule import person1

print(person1["age"])