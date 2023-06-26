depositAmount = float(input());
termInMonths = int(input());
yearInterest = float(input());
interestForOneYear = depositAmount*yearInterest/100;
earnInterest = termInMonths/12*interestForOneYear;
print(earnInterest+depositAmount);