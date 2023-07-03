tabs = int(input())
salary = int(input())
penalty = 0
for tab in range(0, tabs):
    current_tab = input()
    if current_tab == "Facebook":
        penalty = 150
    elif current_tab == "Instagram":
        penalty = 100
    elif current_tab == "Reddit":
        penalty = 50
    salary -= penalty
    penalty = 0
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)
    