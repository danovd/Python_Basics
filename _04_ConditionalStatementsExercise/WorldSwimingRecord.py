import math
recordInSeconds = float(input())
distanceInMeters = float(input())
timeInSecondsForOneMeter = float(input())

timeForAllDistance = distanceInMeters * timeInSecondsForOneMeter
timesDelay = int(distanceInMeters / 15)
totalDelay = timesDelay * 12.5

timeForAllDistance += totalDelay

if timeForAllDistance < recordInSeconds:   # "{:.2f}".format(timeForAllDistance)
    print(f"Yes, he succeeded! The new world record is {'{:.2f}'.format(timeForAllDistance)} seconds.")

else:
    print(f"No, he failed! He was {'{:.2f}'.format(timeForAllDistance - recordInSeconds)} seconds slower.")
