# imports libraries.
import numpy as np
import pandas as pd

#   data    #
exam_data  = {'name': ['Anjum', 'Anali', 'Souria', 'Rockea', 'Imani', 'Mouliya', 'Julie', 'Rana', 'Kavin', 'Bosia'], 
              'score': [15.5, 9, 16.5, np.nan, 9, 30, 17.5, np.nan, 8, 20], 
              'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Exercise_01 #
# 1. For the data set given below construct the DataFrame object
exam_df = pd.DataFrame(exam_data, index=labels)

# 2. Get the first four rows of a DataFrame using indexing method
# print(exam_df[:4])
# print(exam_df.iloc[:4])

##############################################################

# Exercise_02 #
# For the DataFrame created in Exercise_01;
# print(exam_data)

# 1. Select the columns 'score' and 'attempts' in rows 1, 3, 5, 7
# print(exam_df.iloc[[1,3,5,7],[1,2]])

# 2. Count the number of rows and columns without shape attribute
# print(len(exam_df.axes[0]))
# print(len(exam_df.axes[1]))

# 3. Select the rows where the score is between 16 and 20
selection = exam_df['score'].between(16,20)
# print(exam_df[selection])
# print(exam_df[exam_df['score'].between(16,20)])

# 4. select the rows where number of attempts in the examination is less than 2 and score greater than 16 
var1 = exam_df['attempts'] < 2
var2 = exam_df['score'] > 16
cond = var1 & var2
# print(exam_df[cond])

##############################################################

# Exercise_03 #
# For the DataFrame created in Exercise_01;
# 1. Change the score of rows 'C' and 'I' to 16
exam_df.loc[['I','C'],['score']] = 16 
# print(exam_df,"\n")

# 2. Calculate the sum of the examination attempts by the students
print(exam_df['attempts'].sum())

# 3. Add new row with the details name : ‘Rupali’, score: 16, attempts: 2, 
#    qualify: ‘yes’, label: ‘L’. After adding the new row display it and remove it to maintain the original DataFrame.
exam_df.loc['L'] = ['Rupali', 16, 2, 'yes']
# exam_df.drop('L', inplace=True)
# print(exam_df,"\n")

# 4. Remove the last 4 rows and save it as a new DataFrame.  
new_data2 = exam_df.iloc[:-4]
print(new_data2,"\n")
