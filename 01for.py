# Name : any timestable
# Author: Ben Leadbeater
# Date : 03/06/18
# Purpose:
   
number1 = int(input("Please Enter Number for Timestable: "))

for i in range (13):
    print(number1, " *",i,"= ",number1*i)

for i in range (13):
    for j in range (13):
        print ("i *",i, "j = * ",i*j)
