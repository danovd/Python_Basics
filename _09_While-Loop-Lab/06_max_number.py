import sys

numbers = int(input())

count = 0
max_num = -sys.maxsize

while count != numbers:
    new_number = int(input())
    count += 1
    if new_number > max_num:
        max_num = new_number

print(f'{max_num}')
