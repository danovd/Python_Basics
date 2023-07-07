command = input()

sum_prime = 0
sum_non_prime = 0

while command != 'stop':
    num = int(command)
    if num < 0:
        print('Number is negative.')
    else:
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1
        if count == 2:
            sum_prime += num
        elif count > 2:
            sum_non_prime += num
    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
