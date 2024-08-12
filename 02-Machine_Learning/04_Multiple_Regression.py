#########################################
# @file   : 04_Multiple_Regression.py   #
# @brief  : Multiple Regression session #
# @auther : Ziad Mohammed Fathi         #
#########################################

import numpy as np
from sklearn.linear_model import LinearRegression

np.random.seed(42)
x = 3 * np.random.rand(100, 2)
y = 4 + 2 * x[:, 0] + np.random.randn(100)

model = LinearRegression()
model.fit(x, y)

coefficients = model.coef_
intercept = model.intercept_

print("coefficients : ", coefficients)
print("intercept    :  ", intercept)
