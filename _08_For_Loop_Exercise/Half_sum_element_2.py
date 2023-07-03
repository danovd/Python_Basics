import sys

numbers = int(input())
max_number = - sys.maxsize
total_sum = 0
for number in range(1, numbers + 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number
diff = total_sum - max_number
sum_without_max_number = total_sum - max_number
if max_number == diff:
    print(f"Yes\nSum = {diff}")
else:
    print(f"No\nDiff = {abs(max_number - sum_without_max_number)}")
