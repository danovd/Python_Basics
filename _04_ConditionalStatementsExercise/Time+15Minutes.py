hours = int(input())
minutes = int(input())

minutes += 15
totalInMinutes = hours*60 + minutes
if minutes > 59:
    hours += 1
    minutes = minutes - 60

if totalInMinutes >= 24*60:
    hours = hours - 24

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')