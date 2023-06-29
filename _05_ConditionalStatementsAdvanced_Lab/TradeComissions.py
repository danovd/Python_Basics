city = input()
amount = float(input())
isThereAnError = False
commission = 0
if city == "Sofia":
    if 0 <= amount <= 500:
        commission = amount * 0.05
    elif 500 < amount <= 1000:
        commission = amount * 0.07
    elif 1000 < amount <= 10000:
        commission = amount * 0.08
    elif amount > 10000:
        commission = amount * 0.12
    else:
        isThereAnError = True
elif city == "Varna":
    if 0 <= amount <= 500:
        commission = amount * 0.045
    elif 500 < amount <= 1000:
        commission = amount * 0.075
    elif 1000 < amount <= 10000:
        commission = amount * 0.10
    elif amount > 10000:
        commission = amount * 0.13
    else:
        isThereAnError = True
elif city == "Plovdiv":
    if 0 <= amount <= 500:
        commission = amount * 0.055
    elif 500 < amount <= 1000:
        commission = amount * 0.08
    elif 1000 < amount <= 10000:
        commission = amount * 0.12
    elif amount > 10000:
        commission = amount * 0.145
    else:
        isThereAnError = True
else:
    isThereAnError = True
if isThereAnError:
    print("error")
else:
    print(f"{'{:.2f}'.format(commission)}")
