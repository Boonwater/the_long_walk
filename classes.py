""" classes and interaction """

import random
import getch
import sys
from debuff import *

class journey:
    """ the journey """

    def __init__(self, length):
        self.length = length
        print(0, "Your journey begins...")
        print(0, "You have lost yourself deep in the endless forest")
        print(0, "You must now trek the {} miles out".format(self.length))
        input("Enter to continue")
        return self

def travel(journey, pc):
    print(pc.insanity, "as the endless scrapings of hunger and time grow ever louder, it is time to travel")
    print(pc.insanity, "how far will you trek today?")
    print(pc.insanity, "W[More] /S[Less] /Enter[Done]")
    trek = 0
    print(pc.insanity, "trekking _ miles", "\r", 0)
    while True:
        try:
            char = getch.getch()
            if char.lower() == "w":
                trek += 1
                if trek > pc.maxDistance:
                    trek = pc.maxDistance
            elif char.lower() == "s":
                trek -= 1
                if trek < 0:
                    trek = 0

            elif char.lower() == "\n":
                break
            print(pc.insanity, "\x1b[1A\x1b[1A\r[{}{}]".format("#" * (trek), " " * (pc.maxDistance - trek)), "", 0)
            print(pc.insanity, "trekking {} miles    ".format(trek), "", 0)




        except BaseException:
            continue
    attack = trek * 5
    if attack > 20:
        attack = 20
    trap = trek * 2
    if trap > 10:
        trap = 10
    print(0, "", "\n")
    for _ in range(trek):
        if random.randint(0, 100) < attack:
            damage = random.randint(0, 3)
            print(pc.insanity, "you were ambushed! take {} combat damage".format(damage))
            pc.hp -= damage
            if player.checkAlive(pc, journey.length) is "d":
                sys.exit(0)
            continue

        if random.randint(0, 100) < trap:
            damage = random.randint(0, 2)
            print(pc.insanity, "you fell to a trap! take {} damage".format(damage))
            pc.hp -= damage
            if player.checkAlive(pc, journey.length) is "d":
                sys.exit(0)

        journey.length -= 1

    player.consume(pc)
    print(pc.insanity, "you now have a total of {} miles to travel".format(journey.length))
    camp(pc, trek)

class player:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.alive = True
        self.eLVL = 0 # exhaustion level
        self.sLVL = 0 # starvation level
        self.wLVL = 0 # terminal dehydration level
        self.fodLVL = 3  # if this hits 0, starvation sets in
        self.wtrLVL = 1 # if this hits 0, terminal dehydration sets in
        self.strdFOD = 0 # stored food
        self.strdWTR = 0 # stored water
        self.insanity = 0 # fun, right? screws up ui.
        self.maxDistance = 16 # maximum travel distance
        self.sleepNeed = 5
        return self

    def checkDebuff(self):

        if self.sLVL > 0:
            print(self.insanity, "starvation sets in... death approaches")
            self.insanity += 10
            starve(self)

        if self.wLVL > 0:
            print(self.insanity, "you are quickly running out of your invisible water...\nand your sanity.")
            self.insanity += 20
            dehydrate(self)

        if self.eLVL > 0:
            print(self.insanity, "you are so, so, tired... why not sleep forever")
            self.insanity += 5
            exhaust(self)


    def checkAlive(self, length):
        if self.hp <= 0:
            self.alive = False
            print(self.insanity, "{} has perished with {} miles left".format(self.name, length))

        if self.alive is False:
            return "d"

    def consume(self):
        print(self.insanity, "after a full day, a full stomach is it's reward...\nprovided you have the supplies for it.")
        self.strdFOD -= 3
        if self.strdFOD <= 0:
            self.fodLVL + self.strdFOD
            self.strdFOD = 0
            print(self.insanity, "you have no food stored")
            print(self.insanity, "running on fumes... waiting for a quiet death.")
            if self.fodLVL <= 0:
                self.sLVL += 1
                self.fodLVL = 0
                print(self.insanity, "such a little thing to perish for... a bite of bread")


        self.strdWTR -= 1
        if self.strdWTR <= 0:
            self.wtrLVL + self.strdWTR
            print(self.insanity, "you have no stored water")
            print(self.insanity, "as fatigue sets in, a creeping doubt begins...")
            if self.wtrLVL <= 0:
                self.wLVL += 1
                self.wtrLVL = 0
                print(self.insanity, "delerium is a common side effect of terminal dehydration. survival is not.")

        if self.wtrLVL < 0:
            self.wtrLVL = 0

        if self.strdWTR < 0:
            self.strdWTR = 0

        if self.fodLVL < 0:
            self.fodLVL = 0

        if self.strdFOD < 0:
            self.strdFOD = 0

        self.checkDebuff(self)


def camp(player, trek):
    print(player.insanity, "\nIt is time to camp, as the night grows longer.")
    print(player.insanity, "What would you like to do")
    print(player.insanity, "W[Forward] /S[Back] /Enter[Done]")
    actions = ["make fire", "find food", "wound care", "set trap", "menu", "sleep", "suicide"]

    decide = ""
    iterate = -1
    time = 12 - round(trek / 2)
    while time > 0:
        char = getch.getch()
        if char.lower() == "w":
            iterate += 1
            if iterate > 6:
                iterate -= 6
            print(player.insanity, "currently considering {}          ".format(actions[iterate]), "\r", 0)

        if char.lower() == "s":
            iterate -= 1
            while iterate < 0:
                iterate = 6
            print(player.insanity, "currently considering {}          ".format(actions[iterate]), "\r", 0)


        elif char == "\n":
            decide = actions[iterate]
            for _ in actions:
                if decide in _:
                    print(player.insanity, "you have decided to {}       ".format(decide))
                    time -= do(decide, player, time)

            decide = ""



def do(decide, player, time):

    if player.insanity == 100:
        decide = "suicide"
    if decide == "make fire":
        print(player.insanity, "you gather wood and make a fire\nnighttime attacks prevented")
        # no nighttime ambushes
        print(player.insanity, "{} hours left".format(time - 2))
        return 2

    elif decide == "find food":
        print(player.insanity, "food gathered")
        player.strdFOD += random.randint(1, 4)
        player.strdWTR += random.randint(1, 3)
        if player.fodLVL == 0:
            player.fodLVL += player.strdFOD

        if player.wtrLVL == 0:
            player.wtrLVL += player.strdWTR
        print(player.insanity, "{} hours left".format(time - 1))
        return 1

    elif decide == "wound care":
        heal = random.randint(1, 4)
        print(player.insanity, "wounds bandaged successfully, {} hp healed".format(heal))
        player.hp += heal
        print(player.insanity, "{} hours left".format(time - 2))
        return 2

    elif decide == "set trap":
        print(player.insanity, "trap set\nnighttime attacks prevented\npossible food tomorrow morning")
        print(player.insanity, "{} hours left".format(time - 3))
        return 3

    elif decide == "menu":
        print(player.insanity, "log of {}".format(player.name))
        print(player.insanity, "hp [{}]".format(player.hp))
        print(player.insanity, "fod [{}]".format(player.fodLVL))
        print(player.insanity, "wtr [{}]".format(player.wtrLVL))
        print(player.insanity, "strd fod [{}]".format(player.strdFOD))
        print(player.insanity, "strd wtr [{}]".format(player.strdWTR))
        print(player.insanity, "strv level [{}]".format(player.sLVL))
        print(player.insanity, "term dhydrt level [{}]".format(player.wLVL))
        print(player.insanity, "exhaustion level [{}]".format(player.eLVL))
        print(player.insanity, "insanity [{}]".format(player.insanity))
        return 0

    elif decide == "sleep":
        print(player.insanity, "slept {} hours".format(time))
        if time >= 5:
            recovered = round((time - 5) / 2)
            print(player.insanity, "recovered {} lvls exhaustion".format(recovered))
            player.eLVL -= recovered
            if player.eLVL < 0:
                player.eLVL = 0

        elif time < pc.sleepNeed:
            print(player.insanity, "insufficent sleep [{} hrs required] [+1 lvl exhaustion]".format(player.sleepNeed))
            player.eLVL += 1
            player.insanity += 10


        return time

    elif decide == "suicide":
        player.insanity += 40
        print(player.insanity, "insanity sets in... creeping monsters of the mind urge you...")
        player.insanity += 60
        print(player.insanity, "the noose is a comfortable perch.")
        player.insanity += 100
        print(player.insanity, "you stand a monument to your own failure.")
        sys.exit(0)