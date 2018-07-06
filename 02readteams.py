file = open("teams.txt","r")

print("First line")
print(file.readline())
print("Second line")
print(file.readline())
print("Rest of file:")
print(file.read())

file.close()
