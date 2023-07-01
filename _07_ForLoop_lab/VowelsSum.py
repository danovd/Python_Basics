text = input()
result = 0
for char in range(0, len(text)):
    if text[char] == 'a':
        result += 1
    elif text[char] == 'e':
        result += 2
    elif text[char] == 'i':
        result += 3
    elif text[char] == 'o':
        result += 4
    elif text[char] == 'u':
        result += 5
print(result)
