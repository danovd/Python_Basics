import math

typeOfFigure = input()

if typeOfFigure == 'square':
    side = float(input())
    print(side * side)
elif typeOfFigure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    print(side1 * side2)
elif typeOfFigure == 'circle':
    radius = float(input())
    print(radius * radius * math.pi)
elif typeOfFigure == 'triangle':
    length = float(input())
    height = float(input())
    print(length * height / 2)
