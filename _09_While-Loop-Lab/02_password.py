name = input()
password = input()
input_password = input()

while input_password != password:
    input_password = input()

if input_password == password:
    print(f'Welcome {name}!')
