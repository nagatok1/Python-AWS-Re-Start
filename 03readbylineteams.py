file = open("teams.txt","r")

print("3rd Team")
file.readline()
file.readline()
print(file.readline())
file.seek(0)
file.readline()
file.readline()
print(file.readline())

file.close()
