import math

def calc_a(b,c):
    a = math.sqrt(b**2-c**2)
    return a

def calc_b(a,c):
    b = math.sqrt(a**2-c**2)
    return b

def calc_c(a,b):
    c = math.sqrt(a**2+b**2)
    return c

menu_option = 0

while True:

    print("Menu")
    print("1 - Find the length of a given b and c")
    print("2 - Find the length of b given a and c")
    print("3 - Find the length of c given a and b")
    print("9 - Exit")

    menu_option = int(input("Enter Option "))
    if menu_option == 1:
        b= float(input("Please enter length b: "))
        c= float(input("Please enter length c: "))
        print("Length of a= ",calc_a(b,c))
    elif menu_option == 2:
        a= float(input("Please enter length a: "))
        c= float(input("Please enter length c: "))
        print("Length of b= ",calc_b(a,c))
    elif menu_option == 3:
        a= float(input("Please enter length a: "))
        b= float(input("Please enter length b: "))
        print("Length of c= ",calc_c(a,b))
    elif menu_option == 9:
        break
    else:
        print("Input Failed")
