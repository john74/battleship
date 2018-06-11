from collections import defaultdict


class Player:
    def __init__(self):
        self.name = ''
        self.coords = defaultdict(list)


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


while True:

    print("{} select a point to strike!!".format(P1.name))
    player_1_strike = input()
    if player_1_strike in P2.coords.keys():
        print("It is a hit!")
        del P2.coords[player_1_strike]
        if len(P2.coords) == 0:
            print("{} is victorious.He destroyed all of {}'s ships"
                  .format(P1.name, P2.name))
            break
    else:
        print("You missed!")

    print("{} select a point to strike!!".format(P2.name))
    player_2_strike = input()
    if player_2_strike in P1.coords.keys():
        print("It is a hit!")
        del P1.coords[player_2_strike]
        if len(P1.coords) == 0:
            print("{} is victorious.He destroyed all of {}'s ships"
                  .format(P2.name, P1.name))
            break
    else:
        print("You missed!")
