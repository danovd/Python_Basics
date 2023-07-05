needed_money = float(input())
saved_money = float(input())

days_count = 0
spend_count = 0

while True:
    decision = input()
    money_for_all = float(input())
    days_count += 1
    if decision == 'spend':
        spend_count += 1
        saved_money -= money_for_all
        if saved_money < 0:
            saved_money = 0
        if spend_count == 5:
            print(f"You can't save the money.\n{days_count}")
            break
    elif decision == 'save':
        spend_count = 0
        saved_money += money_for_all
        if saved_money >= needed_money:
            print(f"You saved the money for {days_count} days.")
            break
