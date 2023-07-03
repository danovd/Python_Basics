name = input()
points = float(input())
assessors = int(input())

for assessor in range(0, assessors):
    current_assessor = input()
    points_of_current_assessor = float(input())
    points_of_current_assessor = (points_of_current_assessor * len(current_assessor))/2
    points += points_of_current_assessor
    if points > 1250.5:
        break
if points > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {name} you need {(1250.5 - points):.1f} more!")