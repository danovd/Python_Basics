month = input()
nights = int(input())
apartment_price = 0
studio_price = 0
if month == "May" or month == "October":
    studio_price = 50.0
    apartment_price = 65.0
    if 14 >= nights > 7:
        studio_price *= 0.95
    if nights > 14:
        studio_price *= 0.7
elif month == "June" or month == "September":
    studio_price = 75.2
    apartment_price = 68.7
    if nights > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76.0
    apartment_price = 77.0
if nights > 14:
    apartment_price *= 0.9
apartment_price *= nights
studio_price *= nights
print(f"Apartment: {apartment_price:.2f} lv.\nStudio: {studio_price:.2f} lv.")
