budget = float(input())
cards = int(input())
cpus = int(input())
ram = int(input())

sumCards = cards * 250
priceCPU = 0.35 * sumCards
priceRAM = 0.1 * sumCards

theSum = sumCards + priceCPU * cpus + priceRAM * ram

if cards > cpus:
    theSum *= 0.85

if budget >= theSum:
    print(f'You have {"{:.2f}".format(budget - theSum)} leva left!')
else:
    print(f'Not enough money! You need {"{:.2f}".format(theSum - budget)} leva more!')
