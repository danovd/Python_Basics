import math

first = int(input())
second = int(input())
third = int(input())

totalSeconds = first + second + third

minutes = totalSeconds // 60
seconds = totalSeconds % 60

# minutes = math.floor(minutes)

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
