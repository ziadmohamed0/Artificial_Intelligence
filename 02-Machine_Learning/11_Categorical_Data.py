######################################
# @file   : 11_Categorical_Data.py   #
# @brief  : Categorical Data session #
# @auther : Ziad Mohammed Fathi      #
######################################

import pandas as pd

data = {'color': ['red','green','blue','red','green']}
df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=['color'], prefix='color')

print("Original DataFrame: ")
print(df)

print('\nEncoded DataFrame: ')
print(df_encoded)