import pandas as pd
import numpy as np

data = pd.Series(np.arange(6), index=['A','B','C','D','E','F'])
# print(data)
# print(data.drop('A'))
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['A','B','C','D'],
                    columns=['Cairo', 'New Cairo', 'Naser City', 'New Misr'])
print(data)