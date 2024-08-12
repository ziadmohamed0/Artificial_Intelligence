#################################
# @file   : 02_Percentile.py    #
# @brief  : percentile session  #
# @auther : Ziad Mohammed Fathi #
#################################

import numpy as np


def calc_percentile(data, percentile):
    return np.percentile(data, percentile)


data_stat_1 = [10, 15, 20, 25, 30]
result_1 = calc_percentile(data_stat_1, 75)
print("75th percentile : ", result_1)

data_stat_2 = [5, 10, 15, 20, 25, 30, 35]
result_2 = calc_percentile(data_stat_2, 50)
print("50th percentile : ", result_2)
