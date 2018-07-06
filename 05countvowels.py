

words = str(input("Enter Word: "))
search = ["ant","bee","igloo","oscar","unicorn","dragon"]
count_search = 0

for word in search:
    if words in search:
        print(count_search)
        count_search=count_search +1

print("Number of searches in:",words,"= ", count_search)
           
