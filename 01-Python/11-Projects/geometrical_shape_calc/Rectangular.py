#!/bin/python3
import math as m
#----------------------------------------------------------#
# breif : Rectangular class created by ziad mohammed fathi #
#----------------------------------------------------------#

class Rectangular:
    recNumbers = 0
    def __init__(self):
        self.recNumbers += 1
    def Rectangle_area(self,length,width):
        Area = (length * width)
        return Area
    def Rectangle_perimeter(self,length,width):
        Perimeter = (2 * (length + width))
        return Perimeter