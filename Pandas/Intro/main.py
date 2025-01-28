import pandas as pd

print(pd.__version__)

mydataset = {
    'cars' : ['BMW', "Volvo", 'Ford'],
    'passings' : [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)