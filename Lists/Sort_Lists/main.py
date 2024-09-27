list1 = ["apple", "banana", "pineapple", "kiwi", "peru", "mango", "banana", "banana"]
list1.sort()
print(list1)

list1.sort(reverse = True)
print(list1)

def myfunc(n):
    return abs(n - 50)

list1 = [100, 50, 65, 82, 23]
list1.sort(key = myfunc)
print(list1)

list1 = ['banana', 'Orange', 'Kiwi', "cherry"]
list1.sort()
print(list1)
list1.sort(key = str.lower)
print(list1)

list1 = [100, 64 ,92, 82, 15, 36]
list1.reverse()
print(list1)