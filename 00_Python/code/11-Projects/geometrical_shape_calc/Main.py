#!/bin/python3

#-----------------------------------------#
# import library created by ziad mohammed.#
#-----------------------------------------#
import Options


#-----------------#
# started message #
#-----------------#
Options.start()
geometrical = int(input("\nEnter choise : "))                     # input geometrical shape
Options.Area_Perim()
area_perim = int(input("\nEnter choise : "))                     # input geometrical shape
val = Options.chois1(geometrical,area_perim)
print(f'\n=> Value = [{val}]')

