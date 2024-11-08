import os

f = open("demo3.txt", "a")
f.close()

os.remove("demo3.txt")

if os.path.exists("demo3.txt"):
    os.remove("demo3.txt")
else:
    print("File doesn't exists")
    
# delete folder
os.rmdir("test")    # the folder must be empty