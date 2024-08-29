#!/bin/python3

#-----------------------------#
#---------- Metods -----------#
#-----------------------------#
def Calc(num1,num2,ope):
	if ope == '+':
		res = (num1 + num2)
	elif ope == '-':
		res = (num1 - num2)
	elif ope == '*':
		res = (num1 * num2)
	elif ope == '/':
		res = (num1 / num2)
	print('Result = ',res)

print("----- Start Function -----")
Calc(2,4,'-')
print("----- End Function -----")
