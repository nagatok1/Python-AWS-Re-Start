def average(number1,number2,number3):
    if (number1 < 0 or number1 > 100
        or number2 < 0 or number2 > 100
        or number3 < 0 or number3 > 100):
        print("Invalid Mark")
    else:
        average_mark=(number1+number2+number3)/3
        if average_mark >= 65:
            print(average_mark,"Pass")
        else:
            print(average_mark,"Fail")

maths_mark= int(input("Maths Mark= "))
english_mark= int(input("English Mark= "))
it_mark= int(input("IT Mark= "))

print("Maths= ",maths_mark,"English =",english_mark,"IT = ",it_mark)
average(maths_mark,english_mark,it_mark)


                  
        
    
