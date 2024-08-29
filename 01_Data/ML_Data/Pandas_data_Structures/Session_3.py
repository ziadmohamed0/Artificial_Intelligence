import pandas as pd
import numpy as np

from Session_1 import index

stat_capital = {'Karnataka' : 'Bangalore', 'Andrapradesh' : 'Hyderabad',
                'Tamilnadu' : 'Chennai'  , 'Kerala'       : 'thiruvanathapuram', 'Maharastra' : 'Mumbai'}
stat_lang    = {'Karnataka' : 'Kannada'  , 'Andrapradesh' : 'Telugu',
                'Tamilnadu' : 'Tamil'    , 'Kerala'       : 'Malayalam'        , 'Maharastra' : 'Hindi'}
stat_CL = pd.DataFrame({'Capital': stat_capital, 'Language':stat_lang})
# print(stat_CL,"\n")

data = [{'a' : i, 'b' : (2 * i),'c': (3 * i)}for i in range(5)]
data_frame = pd.DataFrame(data)
# print(data,"\n")
# print(data_frame)

stat_CL_1 = pd.DataFrame({'Capital': pd.Series(stat_capital), 'Language':pd.Series(stat_lang)})
# print(stat_CL_1)

data_random = pd.DataFrame(np.random.randn(6, 3), index=['A','B','C','D','E','F'], columns=[1,2,3])
print(data_random)