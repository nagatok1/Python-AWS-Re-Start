print("Menu:")
print("3 - Level 3")
print("4 - Level 4")

examlevel = int(input("Enter Exam Level "))

if examlevel == 3:
    mark = int(input("Enter Level 3 mark: "))
    if mark>65:
        print("Pass")
    else:
        print("Fail")

if examlevel == 4:
    mark= int(input("Enter Level 4 mark: "))
    if mark>50:
        print("Pass")
    else:
        print("Fail")
