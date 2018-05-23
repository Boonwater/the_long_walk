""" classes and interaction """

import random
import getch
import sys

class journey:
    """ the journey """

    def __init__(self, length):
        self.length = length
        print("Your journey begins...")
        print("You have lost yourself deep in the endless forest")
        print("You must now trek the {} miles out".format(self.length))
        input("Enter to continue")
        return self

def travel(journey, pc):
    print("as the endless scrapings of hunger and time grow ever louder, it is time to travel")
    print("how far will you trek today?")
    trek = int(input("> "))
    attack = trek * 5
    if attack > 20:
        attack = 20
    trap = trek * 2
    if trap > 10:
        trap = 10
    for _ in range(trek):
        if random.randint(0, 100) < attack:
            #print("you were ambushed! take no damage(developer)")
            continue

        if random.randint(0, 100) < trap:
            damage = random.randint(0, 2)
            print("you fell to a trap! take {} damage".format(damage))
            pc.hp -= damage
            if player.checkAlive(pc, journey.length) is "d":
                sys.exit(0)

        journey.length -= 1

    print("you now have a total of {} miles to travel".format(journey.length))

class player:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.alive = True
        self.eLVL = 0 # exhaustion level
        self.sLVL = 0 # starvation level
        self.wLVL = 0 # wateration level
        return self

    def checkDebuff(self):
        # todo after debuffs from starvation, etc. are implemented
        print("dev")
        return 0

    def checkAlive(self, length):
        if self.hp <= 0:
            self.alive = False
            print("{} has perished with {} miles left".format(self.name, length))

        if self.alive is False:
            return "d"

def camp(player):
    print("\nIt is time to camp, as the night grows longer.")
    print("What would you like to do")
    actions = ["make fire", "find food", "wound care", "set trap"]
    for _ in actions:
        print(_)
    decide = ""
    while True:
        char = getch.getch()
        print(char, "")
        if char in actions:
            print("you have decided to {}".format(decide))