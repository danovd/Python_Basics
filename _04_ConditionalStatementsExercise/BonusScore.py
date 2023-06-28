num = int(input())
bonus = 0
if num <= 100:
    bonus += 5
elif num <= 1000:
    bonus = 0.2 * num
elif num > 1000:
    bonus = 0.1 * num

if num % 2 == 0:
        bonus += 1
elif num % 10 == 5:
        bonus += 2

print(bonus)
print(bonus + num)
