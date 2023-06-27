numberPens = int(input());
numberMarkers = int(input());
litersDetergent = int(input());
percentDiscount = int(input());

numberPens *= 5.8;
numberMarkers *= 7.2;
litersDetergent *= 1.2;

result = numberPens + numberMarkers + litersDetergent;
result = result - (result * percentDiscount/100);
print(result);