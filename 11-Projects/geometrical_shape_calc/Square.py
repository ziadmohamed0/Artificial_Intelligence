#!/bin/python3
import math as m
#-----------------------------------------------------#
# breif : Square class created by ziad mohammed fathi #
#-----------------------------------------------------#

class Square:
    squareNumbers = 0
    def __init__(self):
        self.squareNumbers += 1
    def square_area(self,side):
        Area = (side * side)
        return Area
    def square_perimeter(self,side):
        Perimeter = (4 * side)
        return Perimeter