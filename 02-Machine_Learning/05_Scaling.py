#################################
# @file   : 05_Scaling.py       #
# @brief  : Scaling session     #
# @auther : Ziad Mohammed Fathi #
#################################

import numpy as np
from sklearn.preprocessing import MinMaxScaler

np.random.seed(42)
data = np.random.rand(100, 1) * 100 + 500
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print("Original Data : ")
print(data[:5])
print("\nScaled Data : ")
print(scaled_data[:5])