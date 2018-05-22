# Secure Containment Breach
import subprocess


def switch(): #for imports
    """ git commit user changer """
    print("init git commit changer tool")
    human = input("moshi moshi?\n>> ").lower() # leave it at this pls

    if human == "cole":
        subprocess.call("git config --global user.email \"cole.leckey.22@gmail.com\"", shell=True)
        subprocess.call("git commit -m \"{}\"".format(input("message\n> ")))

switch()