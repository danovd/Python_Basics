import sys

numbers = int(input())
minimum = sys.maxsize
maximum = - sys.maxsize
for number in range(0, numbers):
    current_number = int(input())
    if current_number < minimum:
        minimum = current_number
    if current_number > maximum:
        maximum = current_number
print(f"Max number: {maximum}")
print(f"Min number: {minimum}")
