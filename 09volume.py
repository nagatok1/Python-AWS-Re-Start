def volume(number1,number2,number3):
    if number1 < 0 or number2 < 0 or number3 < 0:
        print("Invalid Value")
    else:
        volume=(number1*number2*number3)
        print(volume)

length= float(input("Length= "))
width= float(input("Width= "))
height= float(input("Height= "))

volume(length,width,height)
