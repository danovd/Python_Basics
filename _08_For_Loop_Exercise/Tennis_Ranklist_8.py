import math

number_competitions = int(input())
points = float(input())
earned_points = 0
wins = 0
for competition in range(0, number_competitions):
    result_in_current_competition = input()
    if result_in_current_competition == "W":
        earned_points += 2000
        wins += 1
    elif result_in_current_competition == "F":
        earned_points += 1200
    elif result_in_current_competition == "SF":
        earned_points += 720
average_points_per_competition = earned_points / number_competitions
wins = (wins / number_competitions) * 100
points += earned_points
print(f"Final points: {points:.0f}\nAverage points:"
      f" {math.floor(average_points_per_competition)}\n{wins:.2f}%")

