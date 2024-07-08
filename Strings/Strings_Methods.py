#!/bin/python3

#------------------------------#
#------- String Methods -------#
#------------------------------#




#****************************************************#
#******************* Len Function *******************#
#*** breif : len function return length of string ***#
#****************************************************#
str = "ziad mohammed fathi"  # length of string is = 19
print("---------- Len() Method ----------")
mask1 = len(str) # store returned value from len() into variable
print("=> Return = ",mask1)

#****************************************************#
#******************* .upper Method *******************#
#*** breif : .upper Method convert
#             all string to upper case .
#****************************************************#
str = "ziad mohammed fathi"  # ziad moahmmed fathi
mask1 = str.upper() # ZIAD MOHAMMED FATHI MOHAMMED
print("---------- .upper() Method ----------")
print("=> Return = ",mask1)

#****************************************************#
#******************* .lower Method *******************#
#*** breif : .lower Method convert
#             all string to lower case .
#****************************************************#
str = "Ziad Mohammed Fathi"  # Ziad Mohammed Fathi
mask1 = str.lower() # ziad mohammed fathi
print("---------- .lower() Method ----------")
print("=> Return = ",mask1)


#****************************************************#
#******************* .find Method *******************#
#*** breif : .find Method find any character in string
#	     and return number of index.
#****************************************************#
str = "Ziad Mohammed Fathi"  # Ziad Mohammed Fathi
mask1 = str.find('o') # number of index = 6
print("---------- .find() Method ----------")
print("=> Return = ",mask1)

#****************************************************#
#******************* .replace Method *******************#
#*** breif : .replace Method replace slice of string
#            by anouther string.
#****************************************************#
str = "Ziad Mohammed Fathi"  # Ziad Mohammed Fathi
mask1 = str.replace("Fathi","Ziad") #.replace("slice of string","new slice")
print("---------- .replace() Method ----------")
print("string before replaing = ",str)
print("string after replacing = ",mask1)

#****************************************************#
#******************* check if this some string
#		     in main string return true if found
# 		     else return false.
#****************************************************#
str = "Ziad Mohammed Fathi"
print("---------- in Method ----------")
print("Ziad" in str)
print("python" in str)
