n = int(input())
# 1. генерираме всички числа от 1111 до 9999
# 2. за всяко едно число да го разбием на цифри
# 3. проверка дали е специално -> ако е специално го печатаме

for number in range(1111, 10000):
    # разбивка
    first_digit = number // 1000
    second_digit = (number // 100) % 10
    third_digit = (number // 10) % 10
    forth_digit = number % 10

    # специално: 1. n % first == 0; 2. n % second == 0; 3. n % third == 0;
    # 4.  n % forth == 0
    check1 = first_digit != 0 and n % first_digit == 0
    check2 = second_digit != 0 and n % second_digit == 0
    check3 = third_digit != 0 and n % third_digit == 0
    check4 = forth_digit != 0 and n % forth_digit == 0

    if check1 and check2 and check3 and check4:
        print(str(number)+' ', end='')
