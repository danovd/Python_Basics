payment_qty = int(input())

balance = 0
count = 0

while count != payment_qty:
    payment = float(input())
    if payment < 0:
        print('Invalid operation!')
        break
    else:
        balance += payment
        count += 1
        print(f'Increase: {payment:.2f}')

print(f'Total: {balance:.2f}')
