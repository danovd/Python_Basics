priceTrip = float(input())
amountPuzzels = int(input())
amountDolls = int(input())
amountBears = int(input())
amountMinons = int(input())
amountTracks = int(input())

amountToysTotal = amountTracks + amountMinons + amountBears + amountDolls + amountPuzzels
totalSum = amountTracks * 2 + amountPuzzels * 2.6 + amountDolls * 3 + amountBears * 4.1 + amountMinons * 8.2

if amountToysTotal >= 50:
    totalSum *= 0.75

totalSum *= 0.9

if totalSum < priceTrip:
    print(f"Not enough money! {'{:.2f}'.format(priceTrip - totalSum)} lv needed.")
else:
    print(f'Yes! {"{:.2f}".format(totalSum - priceTrip)} lv left.')

