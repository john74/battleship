def align_vertically(letter_index, column_number,
                     ship_length, coords, ship_type):
    board_rows = "ABCDEFGH"[letter_index:ship_length]
    for letter in board_rows:
        coords[letter + column_number].append(ship_type)
    return coords


def align_horizontally(number_index, row_letter,
                       ship_length, coords, ship_type):
    board_columns = "12345678"[number_index:ship_length]
    for number in board_columns:
        coords[row_letter + number].append(ship_type)
    return coords
