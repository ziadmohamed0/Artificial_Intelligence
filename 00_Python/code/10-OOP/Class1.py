#!/bin/python3

#--------------------------------------------------#
#---------------- OOP -> Classes ------------------#
# breif: create class of cars And creat objects    #
# from cars class like BMW .					   #
#--------------------------------------------------#
class cars:
    color = []
    typeCar = []
    price = None
    model = None
    numCar = 0
    def __init__(self):			# Constractor
         	cars.numCar += 1	

    
#*********************#
#***** Objects *******#
#*********************#   
bmw = cars()		# BMW 
marcedes = cars()	# MARCEDICE

#***************#
#***** BMW *****#
#***************#  
bmw.color = ['balck','yellow','gray','green']
bmw.model = 2024
bmw.price = 500000
bmw.typeCar = ['x6','x5','x4','x7','x8']

#*********************#
#***** MARCEDICE *****#
#*********************#  
marcedes.color = ['balck','yellow','gray','green']
marcedes.model = 2023
marcedes.price = 1000000
marcedes.typeCar = ['Benz','c200','B']

#*************************#
#***** Data Printing *****#
#*************************#  
print("\n---------- BMW ------------")
print("BMW Type : ",bmw.typeCar,"\nBMW colors is : ",bmw.color,"\nBMW model : ",bmw.model,"\nBMW Price : ",bmw.price)
print("\n---------- MARCEDICE ------------")
print("MARCEDICE Type : ",marcedes.typeCar,"\nMARCEDICE colors is : ",marcedes.color,"\nMARCEDICE model : ",marcedes.model,"\nMARCEDICE Price : ",marcedes.price)
print("\n---------- Number of Objects ----------")
print(f'Number of Cars is : [{cars.numCar}]')