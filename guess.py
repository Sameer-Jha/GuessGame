from random import randint
from os import system
from time import sleep
from termcolor import cprint, colored
import sys
import os
import readchar

diff = "1"  # Default Difficulty {1-5}
colstrum = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
randcol = lambda: colstrum[randint(0, len(colstrum) - 1)]  # Random Color Generator


class Guess:
    def __init__(self, lowerlimit, upperlimit):
        self.upperlimit = upperlimit
        self.lowerlimit = lowerlimit
        self.number = randint(lowerlimit, upperlimit)
        self.tries = 1

    def get_guess(self):
        try:
            guess = int(
                input(
                    f"Enter your Guess between {self.lowerlimit} and {self.upperlimit} : "
                )
            )

        except:
            print("Invalid Input")

        return guess

    def tries_counter(self):
        self.tries += 1

    def check_guess(self, num):
        if num > self.number:
            cprint("Guess is high", randcol())
            self.tries_counter()
            return False
        elif num < self.number:
            cprint("Guess is low", randcol())
            self.tries_counter()
            return False
        else:
            cprint(f"\n\nGuess Correct\nNo. of tries: {self.tries}", randcol(),attrs=['bold','underline'])
            sleep(4)
            return True

    def game_play(self):
        win = False
        while not (self.check_guess(self.get_guess())):
            pass


def difficulty_handler(diff=1):
    if diff == "1":
        return (0, 100)
    elif diff == "2":
        return (0, 500)
    elif diff == "3":
        return (0, 1000)
    elif diff == "4":
        return (0, 10000)
    elif diff == "5":
        return (0, 1000000)
    else:
        cprint("Mate Be Sane: Enter Valid Inputs PLease", randcol())


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def session():

    global diff

    cprint(
        """
   ______                        ______                   
  / ____/_  _____  __________   / ____/___ _____ ___  ___ 
 / / __/ / / / _ \/ ___/ ___/  / / __/ __ `/ __ `__ \/ _ \\
/ /_/ / /_/ /  __(__  |__  )  / /_/ / /_/ / / / / / /  __/
\____/\__,_/\___/____/____/   \____/\__,_/_/ /_/ /_/\___/ 
__________________________________________________________
__________________________________________________________
""",
        randcol(),
        attrs=["blink", "bold"],
    )
    cprint(
        f"""
Game options:
---- -------
1. Play Game
2. Set Difficulty (Current Difficulty: {diff}/5)
3. Quit
""",
        randcol(),
    )
    cprint("Enter your choice", randcol(), attrs=["bold", "underline"])
    key = readchar.readkey()

    lowerlimit, upperlimit = difficulty_handler(diff)

    if not (key.isalpha()) and 0 < int(key) < 4:

        if key == "1":
            game = Guess(lowerlimit, upperlimit)
            game.game_play()
            del game

        elif key == "2":
            cprint(
                "\nEnter difficulty in the range of 1-5\n1: Noobs\n2: Still a Noob\n3: OK, now we talking \n4: Dude ur F***ed !!\n5: Don't run to your mum crying !!", randcol()
            )
            diff = readchar.readkey()
            lowerlimit, upperlimit = difficulty_handler("1")
            cls()
            session()

        else:
            cls()
            cprint("Thanks for playing !!!",randcol())
            sleep(2)
            cls()
            sys.exit()
    else:
        cprint("Invalid Input", randcol())


if __name__ == "__main__":
    while True:
        cls()
        session()
