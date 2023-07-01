num1 = int(input())
num2 = int(input())
operator = input()
result = 0
isEven = True

if operator == "+":
    result = num1 + num2
    if result % 2 == 0:
        print(f"{num1} + {num2} = {(num1+num2):.0f} - even")
    else:
        print(f"{num1} + {num2} = {(num1+num2):.0f} - odd")
elif operator == "-":
    result = num1 - num2
    if result % 2 == 0:
        print(f"{num1} - {num2} = {(num1-num2):.0f} - even")
    else:
        print(f"{num1} - {num2} = {(num1-num2):.0f} - odd")
elif operator == "*":
    result = num1 * num2
    if result % 2 == 0:
        print(f"{num1} * {num2} = {(num1*num2):.0f} - even")
    else:
        print(f"{num1} * {num2} = {(num1*num2):.0f} - odd")
elif operator == "/":
    if num2 == 0:
       print(f"Cannot divide {num1} by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {(num1/num2):.2f}")
elif operator == "%":
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
    else:
        result = num1 % num2
        symbol = '%'
        print(f"{num1} {symbol} {num2} = {(num1%num2):.0f}")
