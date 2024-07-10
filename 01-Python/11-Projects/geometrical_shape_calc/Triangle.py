#!/bin/python3
import math as m
#-------------------------------------------------------#
# breif : traingle class created by ziad mohammed fathi #
#-------------------------------------------------------#

class Traingle:
    traingleNumbers = 0
    def __init__(self):
        self.traingleNumbers += 1
    def traingle_area(self,base,height):
        Area = (0.5 * (base * height))
        return Area
    def traingle_perimeter(self,sides1,sides2,sides3):
        Perimeter = (sides1 + sides2 + sides3)
        return Perimeter
