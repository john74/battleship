from random import randint


class Player:
    def __init__(self):
        self.name = ''
        self.coords = {}

P1 = Player()
P2 = Player()


for idx, player in enumerate([P1, P2]):
    player.name = input("Player {} set your name: ".format(idx + 1))
    for ship_length in range(1, 5):
        for each_point in range(ship_length):
            coords = input(
                "Player {}: Set coordinates for {}/{} for the ship with length {}"
                .format(player.name, each_point + 1, ship_length, ship_length)
            )
            player.coords[coords] = ship_length
 
first_player = randint(1, 2)
print("Player {} starts first".format(first_player))
