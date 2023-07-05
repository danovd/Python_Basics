# спираме да връщаме ресто: ресто == 0
# връщаме ресто: ресто != 0
change_in_leva = float(input())
change = round(change_in_leva * 100)

count_coins = 0
while change != 0:
    # проверки за монетите
    if change >= 200:
        # 2 +
        change -= 200
        count_coins += 1
    elif change >= 100:
        # 1 -> 1.99
        change -= 100
        count_coins += 1
    elif change >= 50:
        # 0.50 -> 0.99
        change -= 50
        count_coins += 1
    elif change >= 20:
        # 0.20 -> 0.49
        change -= 20
        count_coins += 1
    elif change >= 10:
        # 0.10 -> 0.19
        change -= 10
        count_coins += 1
    elif change >= 5:
        # 0.05 -> 0.09
        change -= 5
        count_coins += 1
    elif change >= 2:
        # 0.02 -> 0.04
        change -= 2
        count_coins += 1
    elif change >= 1:
        # 0.01
        change -= 1
        count_coins += 1
else:
    print(count_coins)
