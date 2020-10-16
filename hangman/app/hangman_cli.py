import os
import sys
from structlog import wrap_logger
import logging


from settings import WORDLIST

from words import Words

log = wrap_logger(logging.getLogger())


def main():
    w = Words()
    w.new_game()

    alive = True
    w.print_display()
    while alive:
        print("Guess a letter: ")
        guess = input()
        if len(guess) > 1:
            print("Just the one letter!")
            continue
        w.guess(guess)
        w.print_display()
        if not w.running:
            sys.exit(0)


if __name__ == "__main__":
    main()
