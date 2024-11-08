# f = open("demo.txt", "r") #Error

# f = open("demofile.txt", "a")

# f = open("demofile.txt", "w")
# f = open("demofile.txt", "x")

f = open("demo.txt")
# print(f.read())

print("\n")

g = open("D:\Imp\Python\File_Handling\Open\demofile.txt")
# print(g.read())

# print(f.readline())
# print(g.readlines())

for x in f:
    print(x)
    
f.close()