# Python does not have built-in support for arrays, lists can be used instead

cars = ['Volvo', 'Ford', 'Honda']

print(cars[0])  # Access

cars[1] = "BMW" # Modify

print(len(cars))# length of array

for x in cars:  # loop through array
    print(x)
    
cars.append('Ferrari')  # Adding element

cars.pop(2)     # removing element
cars.remove('Volvo')

print(cars)