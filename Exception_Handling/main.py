try:
    print(x)
except:
    print("Exception occured")
    
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("Another Error")

try:
    print('Hello')
except:
    print('Error')
else:
    print('Nothing went wrong')
    
try:
    print(x)
except:
    print("Exception occured")
finally:
    print('finally')
    
# x = -1
# if x < 0:
#     raise Exception("Negative no.")

x = -1
if not type(x) is str:
    raise NameError("only str allowed")