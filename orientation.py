def align_vertically(row_letter, column_number ):
    rows = "ABCDEFGH"
    start = coord_letter_index + 1
    finish = ship_length + 1
    for row_letter in rows[start:finish]:
        coords[row_letter+column_number].append(ship_type)


def align_horizontally():
    pass
