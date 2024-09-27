s1 = {'apple', 10, 67.64, True}
print(s1)

# duplicates are ignored
s1 = {'apple', 10, 67.64, True, 'apple'}
print(s1)

# True and 1, and False and 0 are considered same, and are treated as duplicates
s1 = {True, 1, False, 0}
print(s1)

print(type(s1))

s1 = set(('a', 'b', 'c'))
print(s1)

# Access using loop
for x in s1:
    print(x)

# check items
print('b' in s1)
print('b' not in s1)

# Add items
s1 = {'a', 'b', 'c'}
s1.add('d')
print(s1)

# add any iterable obj using update() method
s2 = {'e', 'f'}
list1 = ['g', 'h']
s1.update(s2)
s1.update(list1)
print(s1)

# Remove item
s1 = {'a', 'b', 'c', 'd'}

# remove() method
s1.remove('a')
# s1.remove('88') #Error

# discard() method
s1.discard('c')
s1.discard('88')
print(s1)

# pop() - removes and returns a random item
x = s1.pop()
print(x)
print(s1)

s1.clear()
print(s1)   # o/p:- set() because some existing elements got cleared

s1 = {}
s1.clear()
print(s1)   #o/p:-  {} because set was already empty

del s1