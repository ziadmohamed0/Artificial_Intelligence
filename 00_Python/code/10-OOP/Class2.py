#!/bin/python3

#--------------------------------------------------#
#---------------- OOP -> Classes ------------------#
# breif: create class of cars And creat objects    #
# from cars class like BMW .					   #
#--------------------------------------------------#
class doors :
    objNum = 0
    def __init__(self,color,type,length = 30 ,size = 10) :
        doors.objNum += 1
        self.Colors = color
        self.Types = type
        self.Lengths = length
        self.Sizes = size

#*********************#
#***** Objects *******#
#*********************# 
door1 = doors(
               color = ['green','yellow','red','blue'],
               type = ['wood','steel','plastic'],
               length = 50,
               size = 30
             )
door2 = doors(
               color = ['brown','white','black'],
               type = ['wood','steel','plastic','iron'],
               length = 60,
               size = 20
             )

#*************************#
#***** Data Printing *****#
#*************************#  
print("\n---------- Door [1] ----------")
print(f'=> Colors of Door [1] : {door1.Colors}')
print(f'=> Types  of Door [1] : {door1.Types}')
print(f'=> Length of Door [1] : {door1.Lengths}')
print(f'=> Size   of Door [1] : {door1.Sizes}')

print("\n---------- Door [2] ----------")
print(f'=> Colors of Door [2] : {door2.Colors}')
print(f'=> Types  of Door [2] : {door2.Types}')
print(f'=> Length of Door [2] : {door2.Lengths}')
print(f'=> Size   of Door [2] : {door2.Sizes}')
