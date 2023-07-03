age = int(input())
price_of_aim = float(input())
price_of_single_toy = int(input())
number_of_received_toys = 0
amount_of_money_for_current_birthday = 10
received_money = 0
for year in range(1, age + 1):
    if year % 2 != 0:
        number_of_received_toys += 1
    else:
        received_money += amount_of_money_for_current_birthday
        amount_of_money_for_current_birthday += 10
        received_money -= 1
received_money += (number_of_received_toys * price_of_single_toy)
if received_money >= price_of_aim:
    print(f"Yes! {(received_money - price_of_aim):.2f}")
else:
    print(f"No! {(price_of_aim - received_money):.2f}")
    