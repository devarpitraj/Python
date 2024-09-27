# union() method

s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'f'}
s3 = s1.union(s2)
print(s3)

s3 = s1 | s2
print(s3)

s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'f'}
s3 = {'g', 'h', 'i'}
set1 = s1.union(s1, s2, s3)
print(set1)

set1 = s1 | s2 | s3
print(set1)

# union() allows to join set with other data types but '|' operator doesn't
# s1 = s2.union(list1)  # OK
# s1 = s2 | list1 # Error

# update() method

s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'f'}
s1.update(s2) # s1 |= s2
print(s1)

# intersection() method

s1 = {'a', 'b', True, 'x', False}
s2 = {'c', 'd', 1, 'x', 0}
s3 = s1.intersection(s2)
print(s3)

s3 = s1 & s2
print(s3)

# & only joins sets with sets unlike intersection()

# intersection_update() method

s1.intersection_update(s2)  # s1 &= s2
print(s1)

# difference() method

s1 = {'a', 'b', True, 'x', False}
s2 = {'c', 'd', 1, 'x', 0}
s3 = s1.difference(s2)
print(s3)

s3 = s2 - s1
print(s3)

# - only joins sets with sets unlike difference()

# difference_update() method

s1.difference_update(s2)    # s1 -= s2
print(s1)

# symmetric_difference() method

s1 = {'a', 'b', True, 'x', False}
s2 = {'c', 'd', 1, 'x', 0}
s3 = s1.symmetric_difference(s2)
print(s3)

s3 = s1 ^ s2
print(s3)

# ^ only joins sets with sets unlike symmetric_difference()

# symmetric_difference_update() method

s1.symmetric_difference_update(s2)  # s1 ^= s2
print(s1)