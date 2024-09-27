tup1 = ("A", 65, 78.9, True)
print(tup1)

print(len(tup1))

# Tuple with one item
tup1 = ("A",)   # is a tuple
print(type(tup1))

tup2 = ("A")    # Not a tuple
print(type(tup2))

tup1 = tuple(("A", 'b', 'c'))
print(tup1)

# loop
for x in tup1:
    print(x)
    
for i in range(len(tup1)):
    print(tup1[i])
    
i = 0
while(i < len(tup1)):
    print(tup1[i])
    i = i + 1
 
# Add item   
tup1 = ('A', 'b', 'c')
y = list(tup1)
y.append('d')
tup1 = tuple(y)
print(tup1)

# join 2 tuples
tup1 = ('a', 'b')
tup2 = ('c',)
tup1 += tup2
print(tup1)

# remove item
tup1 = ('a', 'b', 'c', 'd')
y = list(tup1)
y.remove('c')
tup1 = tuple(y)
print(tup1)

# delete tuple
del tup1