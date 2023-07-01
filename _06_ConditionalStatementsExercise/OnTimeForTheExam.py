import math

hour_of_Exam = int(input())
minute_of_Exam = int(input())
hour_of_Arrival = int(input())
minute_of_Arrival = int(input())

total_minutes_Exam = (hour_of_Exam * 60) + minute_of_Exam
total_minutes_Arrival = (hour_of_Arrival * 60) + minute_of_Arrival
difference = abs(total_minutes_Arrival - total_minutes_Exam)

if total_minutes_Arrival == total_minutes_Exam:
    print("On time")
elif total_minutes_Arrival > total_minutes_Exam:
    print("Late ")
    if total_minutes_Arrival < (total_minutes_Exam + 60):
        print(f"{difference:.0f} minutes after the start")
    else:
        if difference % 60 > 9:
            print(f"{math.floor(difference/60)}:{difference % 60} hours after the start")
        else:
            print(f"{math.floor(difference/60)}:0{difference % 60} hours after the start")
elif total_minutes_Arrival < total_minutes_Exam:
    if difference <= 30:
        print(f"On time {difference:.0f} minutes before the start")
    else:
        print("Early ")
    if 30 < difference < 60:
        print(f"{difference:.0f} minutes before the start")
    elif difference >= 60:
        if difference % 60 > 9:
            print(f"{math.floor(difference/60)}:{difference % 60} hours before the start")
        else:
            print(f"{math.floor(difference/60)}:0{difference % 60} hours before the start")
