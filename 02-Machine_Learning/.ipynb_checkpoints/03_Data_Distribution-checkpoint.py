########################################
# @file   : 03_Data_Distribution.py    #
# @brief  : Data Distribution session  #
# @auther : Ziad Mohammed Fathi        #
########################################

import numpy as np
import matplotlib.pyplot as plt

mean = 50
std_dev = 10
sample_size = 1000

data_distribution = np.random.normal(loc=mean, scale=std_dev, size=sample_size)
plt.hist(data_distribution, bins=30, edgecolor='black', density=True)
plt.title('Normal Distribution - Generated data')
plt.xlabel('Val')
plt.ylabel('Probability')
plt.show()
