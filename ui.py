""" ui.py """

import os
import sys
import time
import random
import termios
import termcolor


def printS(insanity, text, end="\n", delay = .02, color=None):
    enableEcho(False)
    for char in text:
        if random.randint(0, 500) < insanity:
            if color is not None:
                sys.stdout.write(termcolor.colored(chr(random.randint(1, 255)).lower(), color))
            else:
                sys.stdout.write(chr(random.randint(1, 255)).lower())
        else:
            if color is not None:
                sys.stdout.write(termcolor.colored(char.lower(), color))
            else:
                sys.stdout.write(char.lower())

        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(end)

    enableEcho(True)

    # flush input
    termios.tcflush(sys.stdin, termios.TCIFLUSH)


def verifyInput(acceptedInput):
    printS("\n> ", "")
    choice = input()
    choice = choice.lower()

    # convert all accepted input to lowercase (disable if need be)
    acceptedInput = [x.lower() for x in acceptedInput]
    firstRun = True

    while choice not in acceptedInput:
        if firstRun:
            replaceLines(1)
            firstRun = False
        else:
            replaceLines(3)

        printS("\nInput invalid!\n", "\n", .02, "red")

        printS("> ", "")
        choice = input()
        choice = choice.lower()

    return choice


def cls():
    os.system("clear")


def replaceLines(linesToDelete):
    cursorOneUp = "\x1b[1A"
    eraseLine = "\x1b[2K"

    for _ in range(linesToDelete):
        sys.stdout.write(cursorOneUp)
        sys.stdout.write(eraseLine)


# from https://gist.github.com/kgriffs/5726314
def enableEcho(enable):
    fd = sys.stdin.fileno()
    new = termios.tcgetattr(fd)
    if enable:
        new[3] |= termios.ECHO
    else:
        new[3] &= ~termios.ECHO