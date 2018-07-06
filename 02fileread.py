file = open("filename.txt","r")

print("First line:")
print(file.readline())
print("Second line:")
print(file.readline())
print("Rest of file:")
print(file.read())
print("Blank line:")
print(file.readline())

file.close()
