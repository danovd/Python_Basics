length = int(input());
width = int(input());
height = int(input());
percent = float(input());

# use width variable for volume instead of creating new one
width *= 0.1;
length *= 0.1;
height *= 0.1;

width *= length * height;
width = width - (width*percent/100);
print(width);