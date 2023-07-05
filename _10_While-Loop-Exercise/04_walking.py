steps_count = 0
goal = 10000

while steps_count < goal:
    command = input()
    if command == 'Going home':
        steps_to_home = int(input())
        steps_count += steps_to_home
        break
    else:
        walked_steps = int(command)
        steps_count += walked_steps

if steps_count >= goal:
    print(f'Goal reached! Good job!')
else:
    print(f'{goal - steps_count} more steps to reach goal.')
