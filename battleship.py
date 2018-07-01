from collections import defaultdict
import random


class Player:
    def __init__(self):
        self.name = ''
        self.coords = defaultdict(list)
        #self.ship_positions = defaultdict(list)
        self.successful_strike = []
        self.chosen_strike = []
        #self.attempts = 0
        self.setup()

    def strike(self, enemy):
        print("{} select a point to strike!!".format(self))
        player_strike = input().upper()
        if player_strike in enemy.coords.keys():
            print("It is a hit!")
            self.successful_strike.append(player_strike)
            del enemy.coords[player_strike]
        else:
            print("You missed")

        # self.attempts += 1
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

    def setup(self):
        set_coords_msg = (
            "set coordinates for {}/{} for the ship with length {}"
        )
        self.name = input("Player set your name: ")
        for ship_length in range(1, 2):
            for each_point in range(ship_length):
                print(set_coords_msg.format(
                    self.name, each_point + 1, ship_length, ship_length
                ))
                coords = input().upper()
                self.coords[coords].append(ship_length)

    def __str__(self):
        return self.name.capitalize()


def main():
    players = [Player(), Player()]
    first_player, second_player = random.sample(players, 2)
    print("{} starts first.".format(first_player))

    while first_player.coords:
        first_player.strike(second_player)
        if not second_player.coords:
            break
        second_player.strike(first_player)

    print("{} is victorious".format(players[0] if players[0].coords
                                    else players[1]))


if __name__ == "__main__":
    main()

# TODO:
# 1. print both boards at the same time
# 2. fix attempts
