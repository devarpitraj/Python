i = 0
while i < 6:
    print(i)
    i += 1
    
i = 10
while i < 16:
    print(i)
    if i == 13: break
    i += 1
    
i = 20
while i < 26:
    i += 1
    if i == 23: continue
    print(i)
    
i = 30
while i < 36:
    print(i)
    i += 1
else:
    print('i == 36')
    
i = 40
while i < 46:
    print(i)
    if i == 43: break
    i += 1
else:   # the else block is not executed when loop is stopped by break statement
    print("this will not be executed")    
