numbers = int(input())
even_position__sum = 0
odd_position_sum = 0
for number in range(0, numbers):
    current_number = int(input())
    if number % 2 == 0:
        even_position__sum += current_number
    else:
        odd_position_sum += current_number

if even_position__sum == odd_position_sum:
    print(f"Yes\nSum = {even_position__sum}")
else:
    print(f"No\nDiff = {abs(even_position__sum - odd_position_sum)}")
