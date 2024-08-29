import pandas as pd                                 # import pandas libaray.

data = pd.read_csv('data/titanic/titanic.csv')              # import file excil sheet.
# print(data)

first_5 = data.head()                               # first 5 elements.
# print(first_5)

first_10 = data.head(n=10)                          # first 10 elements.
# print(first_10)

last_5 = data.tail()                                # last 5 elements.
# print(last_5)

last_10 = data.tail(n=10)                           # last 10 elements.
# print(last_10)

column = data.columns                               # data of Columns.
# print(column)

index = data.index                                  # data of Raws.
# print(index)

# info = data.info()                                # data info.

describe = data.describe()                          # data describe.
print(describe)

shape = data.shape                                  # shaping data (number_raws, number_columns)
# print(shape)

type_data = type(data)                              # type of data
# print(type_data)