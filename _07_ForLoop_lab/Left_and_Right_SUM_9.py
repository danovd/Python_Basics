numbers = int(input())
sum_left = 0
sum_right = 0
for number in range(0, numbers):
    current_number = int(input())
    sum_left += current_number
for number in range(0, numbers):
    current_number = int(input())
    sum_right += current_number
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {abs(sum_left - sum_right)}")
