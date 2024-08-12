###################################
# @file   : 06_Train_Test.py      #
# @brief  : Training Test session #
# @auther : Ziad Mohammed Fathi   #
###################################

import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)
x = np.random.rand(100, 1)
y = 2 * x.squeeze() + 1 + 0.1 * np.random.randn(100)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Training ser Size : ", len(x_train))
print("Testing  ser Size : ", len(x_test))
