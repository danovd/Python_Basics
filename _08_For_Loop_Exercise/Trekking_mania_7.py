number_groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all_climbers = 0
for group in range(0, number_groups):
    number_people_in_current_group = int(input())
    all_climbers += number_people_in_current_group
    if number_people_in_current_group < 6:
        musala += number_people_in_current_group
    elif 5 < number_people_in_current_group < 13:
        monblan += number_people_in_current_group
    elif 12 < number_people_in_current_group < 26:
        kilimandjaro += number_people_in_current_group
    elif 25 < number_people_in_current_group < 41:
        k2 += number_people_in_current_group
    elif 40 < number_people_in_current_group:
        everest += number_people_in_current_group

print(f"{((musala / all_climbers) * 100):.2f}%")
print(f"{((monblan / all_climbers) * 100):.2f}%")
print(f"{((kilimandjaro / all_climbers) * 100):.2f}%")
print(f"{((k2 / all_climbers) * 100):.2f}%")
print(f"{((everest / all_climbers) * 100):.2f}%")
