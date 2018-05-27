""" main file """
from ui import *
import random
import builtins
from classes import *
import getch

builtins.print = printS

def main():
    while True:
        print("...\nThe\nLong\nWalk\n...")
        game()

def game():
    path = journey.__init__(journey, random.randint(0, 100) + 100)
    pc = player.__init__(player, input("name\n> "))
    while path.length > 0:
        travel(path, pc)
    print("you have survived")
    print("shove off")




if __name__ == "__main__":
    main()