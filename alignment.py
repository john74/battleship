def align_vertically(letter_index, column_number,
                     ship_length, coords, ship_type):
    slice_start = letter_index
    slice_end = ship_length + 1
    board_rows = "ABCDEFGH"[slice_start:slice_end]
    for letter in board_rows:
        coords[letter + column_number].append(ship_type)
    return coords


def align_horizontally(number_index, row_letter,
                       ship_length, coords, ship_type):
    slice_start = number_index
    slice_end = ship_length + 1
    board_columns = "12345678"[slice_start:slice_end]
    for number in board_columns:
        coords[row_letter + number].append(ship_type)
    return coords
