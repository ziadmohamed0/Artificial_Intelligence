# 0. imports libraries.
import numpy as np 
import pandas as pd

#################################################

# 1. Create a Series objects using NumPy's linspace and random functions.
data_1 = pd.Series(np.linspace(1, 10, 5))
# print(data_1)

# Without num (Default it is set to 50)
data_2 = pd.Series(np.linspace(1, 10))
# print(data_2.head())

data_Rand_1 = pd.Series(np.random.rand(10))
# print(data_Rand_1)

#################################################

# 2. Create a Series using a list of elements.
Data_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Ser_1 = pd.Series(Data_List)
# print(Ser_1)

#################################################

# 3. For the data given below, get the index and 
#    values after forming a Series object.
Data = pd.Series({'Egypt' : 'Cairo', 'Japan' : 'Tokoyo', 'UK' : 'London'})
index = Data.index
value = Data.values
# print(index,"\n",value)

#################################################

# 4. Create a Series using a range of 10 values and 
#    specify the index explicitly. Use capital alphabets to index explicitly.
Data_Rang = np.arange(10)
index_Val = ['A','B','C','D','E','F','G','H','I','J']
Ser_3 = pd.Series(Data_Rang, index=index_Val)
# print(Ser_3)

#################################################

# 5. For the Exercise_04, 
#    find the 'Shape' and 'Size' of the Series created
Shape_1 = Ser_3.shape
Size_1  = Ser_3.size
# print(Shape_1,"\n",Size_1)

#################################################

# 6. Slice the values of Series created for Exercise_04.
# (a). Slice from 4th index upto the end with step size 3
# (b). Slice the entire Series in reverse order
# (c). Slice the entire Series with step size 2
Slice_a = Ser_3[4::3]
# print(Slice_a)

Slice_b = Ser_3[::-1]
# print(Slice_b)

Slice_d = Ser_3[::2]
# print(Slice_d)

#################################################

# 7. Convert the Series object values 
#    created for Exercise_04 back into the list of values.
#    print(type(Slice_d))
#    print(type(Slice_d.tolist()))

#################################################

# 8. For the data given below, 
#    Construct a Series and add data=[500, 600, 700] to the existing Series.
data_3 = pd.Series(['25', '50', '100', '200', '300', '400'])
data_to_add = pd.Series([500, 600, 700])

data = pd.Series(np.append(arr=data_3,values=data_to_add))
# print(data)

#################################################

# 9. For the Series created in Exercise_08, 
#    get the subset of Series for the condition given below. 
#    condtion = 'values greater than or equal to 100"
new_Ser = pd.to_numeric(data)       # convert to int.

new_sorted = new_Ser[new_Ser >= 100]
# print(new_sorted)

#################################################

# 10. For the data given below constuct a Pandas DataFrame object. 
#     Use labels data to set the index of the DataFrame. 
#     After creating the DataFrame display the summary of the basic information.

exam_data  = {'name': ['Arun', 'Rama', 'Kantharaj', 'James', 'Emily', 'Michael', 
                       'Matthew', 'Laura', 'Kevin', 'Jonas'], 
              'score': [12, 10, 17, np.nan, 9, 30, 15, np.nan, 8, 19], 
              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
              
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

exam_df = pd.DataFrame(exam_data , index=labels)
# print(exam_df,"\n")
# exam_df.info()

#################################################

# 11. Find the names of the people who has scored 
#     greater than 12 in Exercise_10.
# 12. Separate the people with score and without any score 
#     for the Exercise_10.
Sorting = exam_df.loc[exam_df['score'] > 12]
# print(Sorting)

Data_1 = exam_df[exam_df['score'].notnull()]
# print(Data_1,"\n")

Data_1 = exam_df[exam_df['score'].isnull()]
# print(Data_1)

#################################################

# 13. Find the participants who qualify the test and 
#    who didn't qualify the test in Exercise_10
Cond_true = exam_df.loc[exam_df['qualify'] == 'yes']
# print(Cond_true,"\n")

Cond_false = exam_df.loc[exam_df['qualify'] == 'no']
# print(Cond_false)

#################################################

# 14. For the Exercise_10, separete the columns without score 
#    and form a separate DataFrame. 
new_df = exam_df[['name', 'attempts', 'qualify']]
# print(new_df)

#################################################

# 15. For the Exercise_10, 
#    find the number of participants with first attempt.
attempts = exam_df['attempts']
# print(first.value_counts())
var = len(exam_df.loc[exam_df['attempts'] == 1])
# print(var)

#################################################

# 16.  For the Exercise_10 separate the column score and find the top score 
score = exam_df['score']
print(score,"\n")
print(score.max())