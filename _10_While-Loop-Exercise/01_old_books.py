title = input()
books_qty = int(input())

count = 0

while count != books_qty:
    next_title = input()
    if next_title != title:
        count += 1
    else:
        print(f'You checked {count} books and found it.')
        break

if count == books_qty:
    print(f'The book you search is not here!\nYou checked {count} books.')
