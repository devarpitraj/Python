fruits = ['A', 'B', 'C']
for x in fruits:
    print(x)
    
for x in "banana":
    print(x)

for x in fruits:
    print(x)
    if x == 'B': break
    
for x in fruits:
    if x == 'B': continue
    print(x)
    
# range() function
for x in range(6): # by default starts from to 6(not included) and increments by 1
    print(x)
    
for x in range(12, 16): # starts from 12 and ends at 16(not included)
    print(x)
    
for x in range(22, 50, 5): print(x) # starts from 22, ends at 50(not included) and increments by 5

# else statement
for x in range(6): print(x)
else: print('Finished')

# else statement is not invoked if loop is stopped by break statement
for x in range(6):
    print(x)
    if x == 3: break
else: print('Doesn\'t get invoked')

adj = ['A', 'B', "C"]
fruits = ['D', 'E', 'F']
for x in adj:
    for y in fruits:
        print(x, y)
        
# pass statement
for x in [0, 1, 3]:
    pass