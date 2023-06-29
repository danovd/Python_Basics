screening_type = input()
rows = int(input())
cols = int(input())
result = rows * cols
if screening_type == "Premiere":
    result *= 12
elif screening_type == "Normal":
    result *= 7.5
elif screening_type == "Discount":
    result *= 5
print(f"{result:.2f}")
