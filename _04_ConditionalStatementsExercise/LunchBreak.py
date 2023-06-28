import math

name = input()
durationSeries = int(input())
durationRest = int(input())
timeLunch = 1/8 * durationRest
timeRest = 1/4 * durationRest

durationRest -= (timeLunch + timeRest)


if durationRest >= durationSeries:
    print(f'You have enough time to watch {name} and left with {math.ceil(durationRest - durationSeries)} '
          f'minutes free time.')
else:
    print(f"You don't have enough time to watch {name}, you need"
          f" {math.ceil(durationSeries - durationRest)} more minutes.")


