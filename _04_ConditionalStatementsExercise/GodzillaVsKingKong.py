budget = float(input())
statists = int(input())
priceClothesOneStatist = float(input())

totalSum = 0.1 * budget

totalSumStatists = priceClothesOneStatist * statists

if statists > 150:
    totalSumStatists = totalSumStatists - (totalSumStatists * 0.1)

totalSum += totalSumStatists


if totalSum > budget:
    print('Not enough money!')
    print(f'Wingard needs {"{:.2f}".format(totalSum - budget)} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {"{:.2f}".format(budget - totalSum)} leva left.')
