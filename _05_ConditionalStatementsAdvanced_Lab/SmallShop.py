product = input()
city = input()
quantity = float(input())
price = float(0.0);
if city == "Sofia":
    if product == "coffee":
        price = 0.5
    elif product == "water":
        price = 0.8
    elif product == "beer":
        price = 1.2
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.6
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.4
    elif product == "water":
        price = 0.7
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.3
    elif product == "peanuts":
        price = 1.5
elif city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.7
    elif product == "beer":
        price = 1.1
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55

print(price * quantity)
