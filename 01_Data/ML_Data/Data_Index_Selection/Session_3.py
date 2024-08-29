import numpy as np
import pandas as pd

sub  = pd.Series({'Prurgvi' : 'Kannada', 'Pranan' : 'Hindi', 
                  'Pratham': 'English', 'Pravera' : 'Maths', 
                  'Prabu': 'Science'})

total = pd.Series({'Prurgvi' : 60, 'Pranan' : 60, 
                  'Pratham': 60, 'Pravera' : 60, 
                  'Prabu': 60})

min = pd.Series({'Prurgvi' : 30, 'Pranan' : 30, 
                  'Pratham': 30, 'Pravera' : 30, 
                  'Prabu': 30})

obt = pd.Series({'Prurgvi' : 25, 'Pranan' : 35, 
                  'Pratham': 40, 'Pravera' : 60, 
                  'Prabu': 55})

Data = pd.DataFrame({'Sud'   : sub,
                     'T_m'   : total,
                     'Min_m' : min, 
                     'O_m'   : obt})

# print(Data,"\n")

Data['Score'] = Data['O_m'] / Data['T_m']
# print(Data,"\n")

Data['mp_Score'] = Data['Min_m'] / Data['T_m']
print(Data,"\n")

print(Data.T,"\n")