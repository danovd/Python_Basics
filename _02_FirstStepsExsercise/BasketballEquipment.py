yearTax = int(input());
shoes = 0.6 * yearTax;
equip = 0.8 * shoes;
ball = equip/4;
accessories = ball / 5;

yearTax += shoes + equip + ball + accessories;
print(yearTax);