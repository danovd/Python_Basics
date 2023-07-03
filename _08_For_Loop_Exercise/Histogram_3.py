numbers = int(input())
amount_200 = 0
amount_200_400 = 0
amount_400_600 = 0
amount_600_800 = 0
amount_plus_800 = 0
for number in range(0, numbers):
    current_number = int(input())
    if current_number < 200:
        amount_200 += 1
    elif 200 <= current_number < 400:
        amount_200_400 += 1
    elif 400 <= current_number < 600:
        amount_400_600 += 1
    elif 600 <= current_number < 800:
        amount_600_800 += 1
    elif 800 <= current_number:
        amount_plus_800 += 1

print(f"{((amount_200 / numbers) * 100):.2f}%")
print(f"{((amount_200_400 / numbers) * 100):.2f}%")
print(f"{((amount_400_600 / numbers) * 100):.2f}%")
print(f"{((amount_600_800 / numbers) * 100):.2f}%")
print(f"{((amount_plus_800 / numbers) * 100):.2f}%")
