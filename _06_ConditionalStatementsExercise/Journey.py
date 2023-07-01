budget = float(input())
season = input()
expenses = 0
destination = ""
place_for_night = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        expenses = 0.3
        place_for_night = "Camp"
    elif season == "winter":
        expenses = 0.7
        place_for_night = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = 0.4
        place_for_night = "Camp"
    elif season == "winter":
        expenses = 0.8
        place_for_night = "Hotel"
elif budget > 1000:
    destination = "Europe"
    expenses = 0.9
    place_for_night = "Hotel"

print(f"Somewhere in {destination}\n{place_for_night} - {(budget * expenses):.2f}")

