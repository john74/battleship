def print_board(player_name, player_strike):
    board = ""
    for row in "0ABCDEFGH":
        for column in "012345678":
            if row + column == "00":
                board += " "
                continue
            if column == "0":
                board += row
                continue
            if row == "0":
                board += " " + column
                continue

            if row + column in player_strike:
                board += " X"
            else:
                board += "  "
        board += "\n"
    print("{}'s: board\n{}".format(player_name, board))