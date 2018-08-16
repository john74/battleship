from collections import defaultdict
import random
from board import print_board
from validation import validate_point, check_ship_type_amount
from alignment import align_vertically, align_horizontally


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
        print_board(self.name, self.chosen_strike)


    def setup(self):
        fleet = {(1, 5): "Aircraft Carrier", (1, 4): "Battleship",
                 (1, 3): "Cruiser", (2, 2): "Destroyer", (2, 1): "Submarine"}

        self.name = input("Player set your name: ")
        for ship_parameters, ship_type in fleet.items():
            ship_amount, ship_length = ship_parameters
            input_counter = 1
            while True:
                print("Set the starting point for your {}: "
                      .format(ship_type))
                coords = input().upper()
                try:
                    validate_point(coords, self.coords,
                                   check_duplicate=True)
                except Exception as error:
                    print(error)
                    continue

                if ship_length == 1:
                    self.coords[coords].append(ship_type)
                    if check_ship_type_amount(input_counter, ship_amount):
                        input_counter += 1
                        continue
                    break

                print("Set the orientation.(V)ertically/(H)orizontally")
                alignment = input().upper()

                if alignment[0] == "V":
                    letter_index = "ABCDEFGH".index(coords[0])

                    self.coords.update(align_vertically(letter_index,
                                                        coords[1],
                                                        ship_length,
                                                        self.coords,
                                                        ship_type))

                else:
                    number_index = "12345678".index(coords[1])
                    self.coords.update(align_horizontally(number_index,
                                                          coords[0],
                                                          ship_length,
                                                          self.coords,
                                                          ship_type))

                if check_ship_type_amount(input_counter, ship_amount):
                    input_counter += 1
                    continue
                
                break

        print(self.coords)  # TODO: TO BE REMOVED

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
# 4. if a ship type has more than one ships inside the fleet
# user must be asked again to enter coords
