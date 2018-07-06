# Name : 04Decimal.py
# Author: Ben Leadbeater
# Date : 03/06/18
# Purpose: Example of deicmal

from decimal import *

number1 = 1
number2 = 7

print(type(number1))
print(number1 / number2)

number1 = Decimal(1)
number2 = Decimal(7)

print(type(number1))
print(number1 / number2)
