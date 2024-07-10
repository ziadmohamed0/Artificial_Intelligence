#!/bin/python3
import math as m
#-----------------------------------------------------#
# breif : Circle class created by ziad mohammed fathi #
#-----------------------------------------------------#

class Circle:
    circleNumbers = 0
    def __init__(self):
        self.circleNumbers += 1
    def circle_area(self,radius):
        Area = (3.14 * (radius**2))
        return Area
    def circle_perimeter(self,radius):
        Perimeter = (2 * 3.14 * radius)
        return Perimeter