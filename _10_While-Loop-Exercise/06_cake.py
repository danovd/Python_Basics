cake_length = int(input())
cake_weight = int(input())

cake_area = cake_length * cake_weight
cake_pieces_sum = 0

while True:
    cake_pieces = input()
    if cake_pieces == 'STOP':
        cake_pieces_left = cake_area-cake_pieces_sum
        print(f"{cake_pieces_left} pieces are left.")
        break
    else:
        new_cake_pieces = int(cake_pieces)
        cake_pieces_sum += new_cake_pieces
        if cake_pieces_sum > cake_area:
            needed_pieces = cake_pieces_sum - cake_area
            print(f"No more cake left! You need {needed_pieces} pieces more.")
            break
