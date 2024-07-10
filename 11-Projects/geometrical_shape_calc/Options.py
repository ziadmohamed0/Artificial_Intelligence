#!/bin/python3

#-----------------------------------------#
# import library created by ziad mohammed.#
#-----------------------------------------#
from Rectangular import Rectangular
from Circle import Circle
from Triangle import Traingle
from Square import Square

#---------------------------------------------------------------------------------#
# function to display choises for you to select which geometrical shape user need.#
#---------------------------------------------------------------------------------#
def start():
    print("********** Welcome in My Calculator **********\n")
    print("=> Select which eometrical shape you need : ")
    print("--------------------------------------------")
    print("1-Rectangular")
    print("2-Circle")
    print("3-Traingle")
    print("4-Square")

#-------------------------------------------------------------------------------#
# function to display choises for you to select which Area or Perimeter to calc.#
#-------------------------------------------------------------------------------#
def Area_Perim():
        print("\n=> Select Area or Perimeter : ")
        print("------------------------------")
        print("1-Area")
        print("2-Perimeter")

#----------------------------------------------------#
# function to creat object from class the user need .#
#----------------------------------------------------#
def chois1(select1,select2) :

    # Rectangular Choise #
    if select1 == 1:
        rectangel1 = Rectangular()  # Rectangular class from file Rectangular.py.
        wid = int(input("\n->Enter Width  : "))     # get Width.
        Len = int(input("->Enter length : "))       # get length.
        if select2 == 1:
             Value = rectangel1.Rectangle_area(length = Len, width = wid)
        elif select2 == 2:
             Value = rectangel1.Rectangle_perimeter(length = Len, width = wid)
        else:
            print("\n=> Error!!")
            exit(0)

    # Circle Choise #
    elif select1 == 2:
        circle1 = Circle()          # Circle class from file Circle.py.
        rad = int(input("\n->Enter Radius  : "))     # get Radius.
        if select2 == 1:
             Value = circle1.circle_area(radius = rad)
        elif select2 == 2:
             Value = circle1.circle_perimeter(radius = rad)
        else:
            print("\n=> Error!!")
            exit(0)

    # Traingle Choise #
    elif select1 == 3:
        triangle1 = Traingle()      # Triangle class from file Triangle.py.
        if select2 == 1:
             Bas = int(input("\n->Enter Base  : "))     # get Base.
             Hei = int(input("->Enter Height  : "))     # get Height.
             Value = triangle1.traingle_area(base = Bas,height = Hei)
        elif select2 == 2:
             sid1 = int(input("\n->Enter Side 1 : "))     # get Side 1.
             sid2 = int(input("->Enter Side 2 : "))     # get Side 2.
             sid3 = int(input("->Enter Side 3 : "))     # get Side 3.
             Value = triangle1.traingle_perimeter(sides1 = sid1,sides2 = sid2,sides3 = sid3)
        else:
            print("\n=> Error!!")
            exit(0)        

    # Square Choise #
    elif select1 == 4:
        square1 = Square()          # Square class from file Square.py.
        Side = int(input("\n->Enter Side  : "))     # get RadSideius.
        if select2 == 1:
             Value = square1.square_area(side = Side)
        elif select2 == 2:
             Value = square1.square_perimeter(side = Side)
        else:
            print("\n=> Error!!")
            exit(0)

    else:
        print("\n=> Error!!")
        exit(0)
    
    return Value
        