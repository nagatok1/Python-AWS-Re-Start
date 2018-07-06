# Name : calculator.py
# Author: Ben Leadbeater
# Date : 03/06/18
# Purpose:

from decimal import *

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("Calculation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - Squared")
print("6 - Power")

operator = int(input("Enter Calculation: "))

if operator == 1:
    print(Decimal(number1+number2))

elif operator == 2:
    print(Decimal(number1-number2))

elif operator == 3:
    print(Decimal(number1*number2))

elif operator == 4:
    print(Decimal(number1/number2))

elif operator == 5:
    print(Decimal(number1*number1))

elif operator == 6:
    print(Decimal(number1**number2))

else:
    print("Invalid Input")
