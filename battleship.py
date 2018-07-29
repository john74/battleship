from collections import defaultdict
import random
from validation import validate_point
from alignment import align_vertically, align_horizontally
TOTAL_SHIPS = 2  # TODO:to be removed


class Player:
    def __init__(self):
        self.name = ''
        self.coords = defaultdict(list)
        self.successful_strike = []
        self.chosen_strike = []
        self.setup()

    def strike(self, enemy):
        player_strike = input().upper()
        try:
            validate_point(player_strike)
        except Exception as error:
            print(error)
            return self.strike(enemy)

        if player_strike in enemy.coords.keys():
            print("It is a hit!")
            self.successful_strike.append(player_strike)
            del enemy.coords[player_strike]
        else:
            print("You missed")

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
        #  (amount, ship_length: "ship")
        fleet = {(1, 5): "Aircraft Carrier", (1, 4): "Battleship",
                 (1, 3): "Cruiser", (2, 2): "Destroyer", (2, 1): "Submarine"}

        self.name = input("Player set your name: ")
        for ship_length, ship_type in fleet.items():
            while True:
                print("Set the starting point for your {}: "
                      .format(ship_type))
                coords = input().upper()
                try:
                    validate_point(coords, self.coords,
                                   check_duplicate=True)
                    # TODO: impement validation to check
                    # if there is enough space to fit the ship_length
                except Exception as error:
                    print(error)
                    continue

                if ship_length[1] <= 1:
                    self.coords[coords].append(ship_type)
                    break

                print("Set the orientation.(V)ertically/(H)orizontally")
                orientation = input().upper()

                if orientation[0] == "V":
                    letter_index = "ABCDEFGH".index(coords[0])
                    self.coords.update(align_vertically(letter_index,
                                                        coords[1],
                                                        ship_length[1],
                                                        self.coords,
                                                        ship_type))
                    break
                else:
                    number_index = "12345678".index(coords[1])
                    self.coords.update(align_horizontally(number_index,
                                                          coords[0],
                                                          ship_length[1],
                                                          self.coords,
                                                          ship_type))
                    break

    def __str__(self):
        return self.name.capitalize()


def main():
    players = [Player(), Player()]
    first_player, second_player = random.sample(players, 2)

    while first_player.coords:
        print("It's {}'s turn".format(first_player))
        first_player.strike(second_player)
        if not second_player.coords:
            break
        print("It's {}'s turn".format(second_player))
        second_player.strike(first_player)

    print("{} is victorious".format(first_player if first_player.coords
                                    else second_player))


if __name__ == "__main__":
    main()

# TODO:
# 1. print both boards at the same time
# 2. fix attempts
# 3. check if a ship already occupies some blocks and so
# another ship can't be placed
