##########################################
# @file   : 01_Mean_Mode_Med.py          #
# @brief  : Mean, Mode & Median session  #
# @auther : Ziad Mohammed Fathi          #
##########################################

from statistics import mode


# Mean => ((Sum of data) / (Length of data)) #
def Calc_Mean(data):
    value = sum(data) / len(data)
    return value


data_mean = [10, 15, 20, 25, 30]
res_mean = Calc_Mean(data_mean)
print("Mean : ", res_mean)


# Median => middle data #
def Calc_Median(data):
    data.sort()
    n = len(data)
    mid = (n // 2)
    if n % 2:
        median = (data[mid - 1] + data[mid]) / 2
    else:
        median = data[mid]
    return median


data_mid = [10, 15, 20, 25, 30]
res_mid = Calc_Mean(data_mid)
print("Mid  : ", res_mid)


# Mode => middle data #
data_mode = [10, 15, 20, 25, 30, 20, 15, 10]
res_mode = mode(data_mode)
print("Mode : ", res_mode)