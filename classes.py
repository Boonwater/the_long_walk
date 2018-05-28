""" classes and interaction """

import random
import getch
import sys
import ui

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
    print("W[More] /S[Less] /Enter[Done]")
    trek = 0
    print("trekking _ miles", "\r", 0)
    while True:
        try:
            char = getch.getch()
            if char.lower() == "w":
                trek += 1
            elif char.lower() == "s":
                trek -= 1

            elif char.lower() == "\n":
                break

            print("\rtrekking {} miles    ".format(trek), "\r", 0)




        except BaseException:
            continue
    attack = trek * 5
    if attack > 20:
        attack = 20
    trap = trek * 2
    if trap > 10:
        trap = 10
    for _ in range(trek):
        if random.randint(0, 100) < attack:
            damage = random.randint(0, 3)
            print("you were ambushed! take {} combat damage".format(damage))
            pc.hp -= damage
            if player.checkAlive(pc, journey.length) is "d":
                sys.exit(0)
            continue

        if random.randint(0, 100) < trap:
            damage = random.randint(0, 2)
            print("you fell to a trap! take {} damage".format(damage))
            pc.hp -= damage
            if player.checkAlive(pc, journey.length) is "d":
                sys.exit(0)

        journey.length -= 1

    player.consume(pc)
    print("you now have a total of {} miles to travel".format(journey.length))
    camp(pc, trek)

class player:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.alive = True
        self.eLVL = 0 # exhaustion level
        self.sLVL = 0 # starvation level
        self.wLVL = 0 # terminal dehydration level
        self.fodLVL = 9  # if this hits 0, starvation sets in
        self.wtrLVL = 3 # if this hits 0, terminal dehydration sets in
        self.strdFOD = 6 # stored food
        self.strdWTR = 2 # stored water
        return self

    def checkDebuff(self):
        print("strv level [{}]".format(self.sLVL))
        print("wtr level [{}]".format(self.wLVL))
        print("exhaustion level [{}]".format(self.eLVL))
        print("DEVELOPER [non implemented]")

    def checkAlive(self, length):
        if self.hp <= 0:
            self.alive = False
            print("{} has perished with {} miles left".format(self.name, length))

        if self.alive is False:
            return "d"

    def consume(self):
        print("after a full day, a full stomach is it's reward...\nprovided you have the supplies for it.")
        self.strdFOD -= 3
        if self.strdFOD <= 0:
            self.fodLVL + self.strdFOD
            self.strdFOD = 0
            print("you have no food stored")
            print("running on fumes... waiting for a quiet death.")
            if self.fodLVL <= 0:
                self.sLVL += 1
                self.fodLVL = 0
                print("such a little thing to perish for... a bite of bread")


        self.strdWTR -= 1
        if self.strdWTR <= 0:
            self.wtrLVL + self.strdWTR
            print("you have no stored water")
            print("as fatigue sets in, a creeping doubt begins...")
            if self.wtrLVL <= 0:
                self.wLVL += 1
                self.wtrLVL = 0
                print("delerium is a common side effect of terminal dehydration. survival is not.")

        if self.wtrLVL < 0: self.wtrLVL = 0
        if self.strdWTR < 0: self.strdWTR = 0
        if self.fodLVL < 0: self.fodLVL = 0
        if self.strdFOD < 0: self.strdFOD = 0


def camp(player, trek):
    print("\nIt is time to camp, as the night grows longer.")
    print("What would you like to do")
    print("W[Forward] /S[Back] /Enter[Done]")
    actions = ["make fire", "find food", "wound care", "set trap", "menu", "sleep", "suicide"]

    decide = ""
    iterate = -1
    time = 24 - round(trek / 3)
    while time > 0:
        char = getch.getch()
        if char.lower() == "w":
            iterate += 1
            if iterate > 6:
                iterate -= 6
            print("currently considering {}          ".format(actions[iterate]), "\r", 0)

        if char.lower() == "s":
            iterate -= 1
            while iterate < 0:
                iterate = 6
            print("currently considering {}          ".format(actions[iterate]), "\r", 0)


        elif char == "\n":
            decide = actions[iterate]
            for _ in actions:
                if decide in _:
                    print("you have decided to {}       ".format(decide))
                    time -= do(decide, player, time)

            decide = ""



def do(decide, player, time):
    if decide[2] == "k":
        print("you gather wood and make a fire\nnighttime attacks prevented")
        # no nighttime ambushes
        print("{} hours left".format(time - 2))
        return 2

    elif decide == "find food":
        print("food gathered")
        player.strdFOD += random.randint(1, 4)
        player.strdWTR += random.randint(1, 3)
        if player.fodLVL == 0:
            player.fodLVL += player.strdFOD

        if player.wtrLVL == 0:
            player.wtrLVL += player.strdWTR
        print("{} hours left".format(time - 1))
        return 1

    elif decide == "wound care":
        heal = random.randint(1, 4)
        print("wounds bandaged successfully, {} hp healed".format(heal))
        player.hp += heal
        print("{} hours left".format(time - 2))
        return 2

    elif decide == "set trap":
        print("trap set\nnighttime attacks prevented\npossible food tomorrow morning")
        print("{} hours left".format(time - 3))
        return 3

    elif decide == "menu":
        print("log of {}".format(player.name))
        print("hp [{}]".format(player.hp))
        print("fod [{}]".format(player.fodLVL))
        print("wtr [{}]".format(player.wtrLVL))
        print("strd fod [{}]".format(player.strdFOD))
        print("strd wtr [{}]".format(player.strdWTR))
        print("strv level [{}]".format(player.sLVL))
        print("term dhydrt level [{}]".format(player.wLVL))
        print("exhaustion level [{}]".format(player.eLVL))
        return 0

    elif decide == "sleep":
        print("slept {} hours".format(time))
        if time >= 5:
            recovered = round((time - 5) / 2)
            print("recovered {} lvls exhaustion".format(recovered))
            player.eLVL -= recovered
            if player.eLVL < 0:
                player.eLVL = 0

        elif time < 5:
            print("insufficent sleep [5 hrs required] [+1 lvl exhaustion]")
            player.eLVL += 1

        return time

    elif decide == "suicide":
        print("insanity sets in... creeping monsters of the mind urge you...")
        print("the noose is a comfortable perch.")
        print("you stand a monument to your own failure.")
        sys.exit(0)