import time
import datetime

print("Enter First Time (Input 0 in all Fields for time conversion")
minutes_1 = int(input("Minutes: "))
hours_1 = int(input("Hours: "))
days_1 = int(input("Days: "))

print("Enter Second Time (Input 0 in all Fields for time Conversion")
minutes_2 = int(input("Minutes: "))
hours_2 = int(input("Hours: "))
days_2 = int(input("Days: "))

duration_1 = datetime.timedelta(days=days_1,hours=hours_1,minutes=minutes_1)
duration_2 = datetime.timedelta(days=days_2,hours=hours_2,minutes=minutes_2)              
addtimes = (duration_1 + duration_2)
timediff = duration_1 - duration_2
timeseconds = addtimes.total_seconds()
timeminutes = addtimes.total_seconds()/60
timehours = addtimes.total_seconds()/3600
timedays = addtimes.total_seconds()/86400

print(duration_1, duration_2)
print("Calculation: ")
print("1 - Add")
print("2 - Difference")
print("3 - Convert Total Time to Days")
print("4 - Convert Total Time to Hours")
print("5 - Convert Total Time to Minutes")
print("6 - Convert Minutes to Time")
print("7 - Convert Hours to Time")
print("8 - Convert Days to Time")

operator = False

while operator == False:
    operator = int(input("Enter Calculation: "))
    if operator == 1:
        print(duration_1, "+", duration_2, "=", addtimes)

    elif operator == 2:
        print("Difference between ", duration_1, "+", duration_2, "=", timediff)

    elif operator == 3:
        print(addtimes, "in days = ", timedays)

    elif operator == 4:
        print(addtimes, "in Hours =", timehours)

    elif operator == 5:
        print(addtimes, "in Minutes =", timeminutes)

    elif operator == 6:
        minutes_i = int(input("Input Minutes to Convert to Time: "))
        days_m = int(minutes_i / 1440)
        remain_days = days_m % 3600
        hours_m = int(remain_days / 24)
        remain_hours = (remain_days % 24)
        minutes_m = int(remain_hours / 60)
        print(days_m,"Days",hours_m,"Hours",minutes_m,"Minutes")

    elif operator == 7:
        hours_i = int(input("Input Hours to Convert to Time: "))
        minutes_h = hours_i*60
        days_h = int(minutes_h / 1440)
        remain_days2 = days_h % 3600
        hours_h = int(remain_days2 / 24)
        remain_hours2 = (remain_days2 % 24)
        minutes_h = int(remain_hours2 / 60)
        print(days_h,"Days",hours_h,"Hours",minutes_h,"Minutes")

    elif operator == 8:
        days_i = int(input("Input Days to Convert to Time: "))
        minutes_d = days_i*1440
        days_d = int(minutes_d / 1440)
        remain_days3 = days_d % 3600
        hours_d = int(remain_days3 / 24)
        remain_hours3 = (remain_days3 % 24)
        minutes_d = int(remain_hours3 / 60)
        print(days_d,"Days",hours_d,"Hours",minutes_d,"Minutes")

    else:
        Print("Invalid Input")

operator = False
