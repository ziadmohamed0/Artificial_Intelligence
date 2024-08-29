import pandas as pd
import numpy as np

# -------------------------------------------------------------------------------- #

# 1. Create a Series objects using NumPy's linspace and random functions.
data  = pd.Series(np.linspace(1,10,5))
# print(data)
data = pd.Series(np.random.rand(10))
# print(data)

# -------------------------------------------------------------------------------- #

# 2. Create a Series using a list of elements.
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(data)

# -------------------------------------------------------------------------------- #

# 3. For the data given below, get the index and 
#    values after forming a Series object.
data = pd.Series({'Egypt' : 'Cairo', 'Japan' : 'Tokoyo', 'UK' : 'London'})
# print(data.index,"\n\n",data.values)

# -------------------------------------------------------------------------------- #

# 4. Create a Series using a range of 10 values and 
#    specify the index explicitly. Use capital alphabets to index explicitly.
data = pd.Series(range(10),index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# print(data)
# -------------------------------------------------------------------------------- #

# 5. For the Exercise_04, 
#    find the 'Shape' and 'Size' of the Series created.

# print(data.shape,"\n",data.size)

# -------------------------------------------------------------------------------- #

# 6. Slice the values of Series created for Exercise_04.

# print(data)

# (a). Slice from 4th index upto the end with step size 3

# print(data[4::3])

# (b). Slice the entire Series in reverse order

# print(data[::-1])

# (c). Slice the entire Series with step size 2

# print(data[::2])

# -------------------------------------------------------------------------------- #

# 7. Convert the Series object values 
#    created for Exercise_04 back into the list of values.

# print(type(data))
# print(data.to_list())

# -------------------------------------------------------------------------------- #

# 8. For the data given below, 
#    Construct a Series and add data=[500, 600, 700] to the existing Series.
data = pd.Series(['25', '50', '100', '200', '300', '400'])
dataADD = pd.Series([500, 600, 700])
data = pd.Series(np.append(arr = data, values = dataADD))
# print(data)

# -------------------------------------------------------------------------------- #

# 9. For the Series created in Exercise_08, 
#    get the subset of Series for the condition given below. 
#    condtion = 'values greater than or equal to 100".
data = pd.to_numeric(data)
# print(data[data >= 100])

# -------------------------------------------------------------------------------- #

# 10. For the data given below constuct a Pandas DataFrame object. 
#     Use labels data to set the index of the DataFrame. 
#     After creating the DataFrame display the summary of the basic information.
data  = {'name': ['Arun', 'Rama', 'Kantharaj', 'James', 'Emily', 'Michael', 
                       'Matthew', 'Laura', 'Kevin', 'Jonas'], 
              'score': [12, 10, 17, np.nan, 9, 30, 15, np.nan, 8, 19], 
              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
              
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
 
data_df = pd.DataFrame(data=data, index=labels)
# print(data_df)
# data_df.info()

# -------------------------------------------------------------------------------- #

# 11. Find the names of the people who has scored 
#     greater than 12 in Exercise_10.
score_sorting = data_df.loc[data_df['score'] > 12]
# print(score_sorting)

# -------------------------------------------------------------------------------- #

# 12. Separate the people with score and without any score 
#     for the Exercise_10.


# -------------------------------------------------------------------------------- #

# 13. Find the participants who qualify the test and 
#    who didn't qualify the test in Exercise_10.

# 14. For the Exercise_10, separete the columns without score 
#    and form a separate DataFrame. 

# 15. For the Exercise_10, 
#    find the number of participants with first attempt.