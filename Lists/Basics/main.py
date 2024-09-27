list1 = ["apple", 25, 78.53, True]
print(list1[len(list1) - 1])
print(list1[1:3])
print(list1[1:])
print(list1[:3])
print("25" in list1)

list1[2] = "new"
print(list1)

list1[1:3] = [45, "A"]
print(list1)

list1[1:3] = [65, "b", "c"] #more inserted than replaced
print(list1)

list1[1:3] = [74] #less inserted than replaced
print(list1)

list1.insert(3, 88)
print(list1)

list1.append("X")
print(list1)

list2 = ["I", "P"]
list1.extend(list2)
print(list1)

tuple1 = ("L", "K")
list1.extend(tuple1)    # extend() method can append any iterable object like tupes, sets, dictionaries, etc
print(list1)

list1.remove('apple')
print(list1)

list1.pop(3)
print(list1)

list1.pop()
print(list1)

del list1[3]
print(list1)

list2 = ['a', 'b']
del list2   #deletes the complete list
# print(list2)    # Error

list2 = ['a', 'b']
list2.clear()   # list remains but no content
print(list2)
print('\n')

for x in list1:
    print(x)
print('\n')

for i in range(len(list1)):
    print(list1[i])
print('\n')

i = 0
while i < len(list1):
    print(list1[i])
    i = i + 1
print('\n')

[print(x) for x in list1]
print('\n')

