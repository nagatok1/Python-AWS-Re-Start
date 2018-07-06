file = open("filename.txt","r")

print("First line:")
print(file.readline())
file.seek(0)
print("First line again")
print(file.readline())
file.seek(35,0)
print("From the 25th character...")
print(file.read())

file.close()
