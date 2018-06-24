from collections import defaultdict


class Player:
    def __init__(self):
        self.name = ''
        self.coords = defaultdict(list)
        self.successful_strike = []
        self.chosen_strike = []
        self.attempts = 0

    def strike(self, enemy):
        print("{} select a point to strike!!".format(self.name))
        player_strike = input().upper()
        if player_strike in enemy.coords.keys():
            print("It is a hit!")
            self.successful_strike.append(player_strike)
            del enemy.coords[player_strike]
        else:
            print("You missed")

        self.attempts += 1
        self.chosen_strike.append(player_strike)
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
                    continue
                if row == "0":
                    board += " " + column
                    continue

                if row + column in self.chosen_strike:
                    board += " X"
                else:
                    board += "  "
            board += "\n"
        print("{}'s: board\n{}".format(self.name, board))


P1 = Player()
P2 = Player()

total_ships = int(input("Enter the total number of ships: "))

for idx, player in enumerate([P1, P2]):
    player.name = input("Player {} set your name: ".format(idx + 1))
    for ship_length in range(1, total_ships):
        for each_point in range(ship_length):
            print("{} set coordinates for {}/{} for the ship with length {}"
                  .format(player.name, each_point + 1,
                          ship_length, ship_length))
            coords = input().upper()
            player.coords[coords].append(ship_length)


while P1.coords:
    P1.strike(P2)
    if not P2.coords:
        break
    P2.strike(P1)

print("{} is victorious".format(P1.name if P1.coords else P2.name))
