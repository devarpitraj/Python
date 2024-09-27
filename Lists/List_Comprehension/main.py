fruits = ["apple", "banana", "pineapple", "kiwi", "peru", "mango", "banana", "banana"]

newlist = [x for x in fruits if 'a' not in x]
print(newlist)

newlist = [x.upper() for x in fruits if 'a' in x]
print(newlist)

newlist = ['hi' for x in fruits]
print(newlist)

newlist = [x if x == "banana" else "orange" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)