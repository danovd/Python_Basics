n = int(input())

counter = 0

for x1 in range(0, n+1):
    for x2 in range(0, n+1):
        for x3 in range(0, n+1):
            if x1+x2+x3 == n:
                counter += 1

print(f'{counter}')
