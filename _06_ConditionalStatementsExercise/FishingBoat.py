budget = int(input())
season = input()
number_fishers = int(input())
rent_of_boat = 0;
discount = 0;
if season == "Spring":
    rent_of_boat = 3000
elif season == "Summer" or season == "Autumn":
    rent_of_boat = 4200
elif season == "Winter":
    rent_of_boat = 2600

if 1 <= number_fishers <= 6:
    discount = 0.1
elif 6 < number_fishers <= 11:
    discount = 0.15
elif number_fishers >= 12:
    discount = 0.25

rent_of_boat = rent_of_boat - (rent_of_boat * discount)

if number_fishers %2 == 0 and season != "Autumn":
    discount = 0.05
else:
    discount = 0

rent_of_boat = rent_of_boat - (rent_of_boat * discount)

if budget >= rent_of_boat:
    print(f"Yes! You have {(budget - rent_of_boat):.2f} leva left.")
else:
    print(f"Not enough money! You need {(rent_of_boat - budget):.2f} leva.")