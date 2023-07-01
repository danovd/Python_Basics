days = int(input())
types = input()
estimate = input()
discount = 0
price = 0
if types == "room for one person":
    price = 18
elif types == "apartment":
    price = 25
    if days <= 10:
        discount = 0.3
    elif 10 < days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.5
elif types == "president apartment":
    price = 35
    if days <= 10:
        discount = 0.1
    elif 10 < days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.2
result = price - (price * discount)
result *= (days - 1)

if estimate == "positive":
    result *= 1.25
elif estimate == "negative":
    result *= 0.9

print(f"{result:.2f}")
