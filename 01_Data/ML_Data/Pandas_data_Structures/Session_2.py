import pandas as pd

List = [1.0, 2.0, 0.3, 0.4, 0.5, 0.6]
print(pd.Series(List))

print("")

Dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F'}
print(pd.Series(Dic))

print("")

data = pd.read_csv('data/Students_Marks/student_marks.csv')
print(data)

print("")

# print(data['name'])