chicken = int(input());
fish = int(input());
vegetarian = int(input());

chicken *= 10.35;
fish *= 12.40;
vegetarian *= 8.15;

# use chicken variable instead of creating new one

chicken += fish;
chicken += vegetarian;

chicken *= 1.2;
chicken += 2.5;

print(chicken);