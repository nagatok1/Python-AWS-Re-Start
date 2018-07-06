# Name : 04list.py
# Author: Ben Leadbeater
# Date : 03/06/18
# Purpose:

fruit = ["apple","pineapple","pen"]
print (fruit)

print(fruit[1])

fruitset= {"Orange","Mango","Pear",}
print(fruitset)
fruitset.add("Peach")
print(fruitset)
fruitset.add("Peach")
print(fruitset)

fruitprice = {}
fruitprice["apple"] = 0.99
fruitprice["orange"] = 3.50
fruitprice["pineapple"] = 99.99
RumpelstiltskintheFourth = "Priceless"

print ("£",fruitprice["orange"])
print (RumpelstiltskintheFourth)
print ("£",fruitprice["pineapple"])
print ("WTF it's a piece of fucking fruit\nFucking farmers ripping us off\nRobbing Bastards")

Total= (fruitprice["apple"] + fruitprice["orange"])

print ("Apple + Orange = " + "£", Total)
print ("Much Better")
