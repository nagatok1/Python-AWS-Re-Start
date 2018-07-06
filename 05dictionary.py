# Name : 05dictionary
# Author: Ben Leadbeater
# Date : 03/06/18
# Purpose:

name = {}
name["Jack"] = 23
name["James"] = 17
name["Joe"] = 19
name["John"] = 20
name["Rumpelstiltskin the Fourth"] = 99
print(name)
print(name["John"])

if "John" in name:
    print(name["John"])
else:
    print ("Not in name")
