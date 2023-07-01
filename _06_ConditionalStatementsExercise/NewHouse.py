type_flower = input()
number_flowers = int(input())
budget = int(input())
discount = 0;
price_of_Flower = 0
if type_flower == "Roses":
    price_of_Flower = 5
    if number_flowers > 80:
        discount = 0.10
elif type_flower == "Dahlias":
    price_of_Flower = 3.8
    if number_flowers > 90:
        discount = 0.15
elif type_flower == "Tulips":
    price_of_Flower = 2.8
    if number_flowers > 80:
        discount = 0.15
elif type_flower == "Narcissus":
    price_of_Flower = 3
    if number_flowers < 120:
        discount = -0.15
elif type_flower == "Gladiolus":
    price_of_Flower = 2.5
    if number_flowers < 80:
        discount = -0.20
result = number_flowers * price_of_Flower
result = result - (result * discount)
if budget >= result:
    print(f"Hey, you have a great garden with {number_flowers:.0f} {type_flower} and {(budget - result):.2f}"
          f" leva left.")
else:
    print(f"Not enough money, you need {(result-budget):.2f} leva more.")