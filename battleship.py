from collections import defaultdict


class Player:
    def __init__(self):
        self.name = ''
        self.coords = defaultdict(list)
        self.stricken = []

    def strike(self, enemy):
        print("{} select a point to strike!!".format(self.name))
        player_strike = input()
        if player_strike in enemy.coords.keys():
            print("It is a hit!")
            del enemy.coords[player_strike]
        else:
            print("You missed")

        self.stricken.append(player_strike)
        self.print_board()

    def print_board(self):
        board = ""
        for row in "0ABCDEFGH":
            for column in "012345678":
                if row + column == "00":
                    board += " "
                    continue
                if column == "0":
                    board += row
                if row == "0":
                    board += column

                if row + column in self.stricken:
                    board += "X"
                else:
                    board += " "
            board += "\n"
        print("{}'s: board\n {}".format(self.name, board))


P1 = Player()
P2 = Player()


for idx, player in enumerate([P1, P2]):
    player.name = input("Player {} set your name: ".format(idx + 1))
    for ship_length in range(1, 5):
        for each_point in range(ship_length):
            coords = input(
                "Player {}: Set coordinates for {}/{} for the ship with length"
                " {}: "
                .format(player.name, each_point + 1, ship_length, ship_length)
            )
            player.coords[coords].append(ship_length)


while P1.coords:
    P1.strike(P2)
    if not P2.coords:
        break
    P2.strike(P1)

print("{} is victorious".format(P1.name if P1.coords else P2.name))
