file = open("teams.txt","r")

file.readline()
file.readline()
file.read(2)
print("2nd and 3rd Characters of 3rd Team: ")
print(file.read(2))

file.close()

