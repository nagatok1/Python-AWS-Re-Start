def Exam_grade(level,mark):
    if level < 1 or level > 4:
        print("Invalid Level")
    elif mark < 0 or mark > 100:
        print("Invalid Mark")
    elif level == 1 or level == 2:
        if mark >= 85:
            print("Distinction")
        elif mark >= 75:
            print("Merit")
        elif mark >=65:
            print("Pass")
        else:
            print("Fail")
    elif level == 3:
        if mark >= 80:
            print("Distinction")
        elif mark >= 70:
            print("Merit")
        elif mark >= 60:
            print("Pass")
        else:
            print("Fail")
    elif level == 4:
        if mark >= 70:
            print("Distinction")
        elif mark >= 60:
            print("Merit")
        elif mark >= 50:
            print("Pass")
        else:
            print("Fail")

level = int(input("Please Enter Exam Level= "))
mark = int(input("Please Enter Mark= "))

Exam_grade(level,mark)





