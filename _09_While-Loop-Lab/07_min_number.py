import sys

numbers = int(input())

count = 0
min_num = sys.maxsize

while count != numbers:
    new_number = int(input())
    count += 1
    if new_number < min_num:
        min_num = new_number

print(f'{min_num}')
