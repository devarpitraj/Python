f = open("demo2.txt", "a")
f.write("Hello there")
f.close()

f = open("demo2.txt", "r")
print(f.read())
f.close()

f = open("demo2.txt", "w")
f.write("overwrites the file")
f.close()

f = open("demo2.txt", "r")
print(f.read())
f.close()