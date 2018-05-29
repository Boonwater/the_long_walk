""" main file """
import random
import builtins
from classes import *
import getch
from ui import *

builtins.print = printS

def main():
    """ introductory function """
    while True:
        print(0, "...\nThe\nLong\nWalk\n...")
        game()

def game():
    """ the entire game """
    path = journey.__init__(journey, random.randint(0, 100) + 100)
    pc = player.__init__(player, input("name\n> "))
    while path.length > 0:
        travel(path, pc)
    print(0, "you have survived")
    print(0, "screw off.")



if __name__ == "__main__":
    main()