import pandas as pd
import numpy as np

data = pd.Series([10,20,30,40,50,60], index = ['A','B','C','D','E','F'])
print(data,"\n")

if 'A' in data:
    print("True\n")
else:
    print("False\n")

# print(data.keys())
# print(data.items())
print(list(data.items()))