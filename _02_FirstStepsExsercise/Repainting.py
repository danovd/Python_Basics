nylon = int(input());
paint = int(input());
thinner = int(input());
hoursForWork = int(input());

nylon *= 1.5;
paint *= 14.5;
thinner *= 5;

paint *= 1.1;
nylon += 3;
result = nylon + paint + thinner;
result += 0.4;

hoursForWork *= result*0.3;
result += hoursForWork;

print(result);
