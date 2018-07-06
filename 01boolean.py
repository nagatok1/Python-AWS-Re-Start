# Name : 01boolean
# Author: Ben Leadbeater
# Date : 03/06/18
# Purpose:
number1= float(input("please enter first number: "))
number2= float(input("please enter second number: "))

if number1 > number2:
    number1bigger = True
else:
    number1bigger = False

print("number1 bigger:",number1bigger)

if number1bigger:
                 print("number1 bigger")
else:
     print("number1 not bigger")
