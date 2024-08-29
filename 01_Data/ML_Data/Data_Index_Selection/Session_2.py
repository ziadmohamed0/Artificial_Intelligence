import pandas as pd
import numpy as np

data = pd.Series([10,20,30,40,50,60], index = ['A','B','C','D','E','F'])

print(data,"\n")
print(data['A':'D'],"\n")
print(data[1:4],"\n")
print(data[(data > 20) & (data < 50)])