#---------------------------------------#
# breif : mean & Madian & Mode Session. #
#---------------------------------------#
from statistics import mode

#function Mean -> avarage
def Calc_Mean(data):
    mean = sum(data) / len(data)
    return mean

#function Mean -> avarage
def Calc_median(data):
    data.sort()
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        median = ((data[mid - 1] + data[mid]) / 2)
    else :
        median = data[mid]
    return median

#    Data
data_set = [10,15,20,25,30,20,15,10]
print("----- Mean , Median , Mode -----\n")
print("Data   : ",data_set)

#   Mean
mean_Res = Calc_Mean(data_set)
print("Mean   : ", mean_Res)

#   Median
median_Res = Calc_median(data_set)
print("Median : ",median_Res)

#   Mode
mode_Res = mode(data_set)
print("Mode   : ",mode_Res)