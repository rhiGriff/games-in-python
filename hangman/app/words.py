import sys
from settings import WORDLIST, MIN_WORD_LENGTH, MAX_WORD_LENGTH, CHEAT

from structlog import wrap_logger
import logging

from random import randint

log = wrap_logger(logging.getLogger())

MAX_GUESSES = 6
BLANK = "░"

# The gibbet and hanging man are made from asscii sequences.
# As the guesses progress, the man's bits are substituted into the positions
# indicated in their tuples
ASSCII_GIBBET = " ╬═══╬═\n ║   │\n ║    \n ║     \n ║     \n═╩══════"
MAN_BITS = [("o", 20), ("|", 27), ("/", 26), ("\\", 28), ("/", 34), ("\\", 36)]


class Words:
    def __init__(self):
        self.words = []
        self.num = 0
        self._state = []
        self._guesses = 0
        self._guessed = {}
        self.running = False

        self._load_list()

    def new_game(self):
        log.debug("Starting new game")
        self._state = []
        self._guesses = 0
        self._guessed = {}
        self.running = True

        self.chosen = self.choose()

    def _load_list(self):
        log.debug("Attempting to open and parse wordlist")
        try:
            wl = open(WORDLIST, "r")
        except Exception as e:
            log.error("Failed to open wordlist", file=WORDLIST, ex=e)
            return

        all_words = wl.read().splitlines()

        log.debug("Successfully read wordlist", num_words=len(all_words))

        # Filter the word list based on MIN and MAX settings
        self.words = [
            w
            for w in all_words
            if len(w) >= MIN_WORD_LENGTH and len(w) <= MAX_WORD_LENGTH
        ]
        self.num = len(self.words)
        log.debug(
            "Wordlist filtered",
            min=MIN_WORD_LENGTH,
            max=MAX_WORD_LENGTH,
            num_words=self.num,
        )

    def end_game(self, win):
        if win:
            print("Congratulations!")
        else:
            self._reveal()
            print("Oh dear! Looks like you lost")
        self.running = False
        return

    def guess(self, guess):
        """Guess performs a guess on the chosen word and increments the number
        of guesses that have been performed if it's not correct"""
        if guess in self._guessed:
            print("You already guessed that one, try again!")
            return

        self._guessed[guess] = True

        matched = False
        num_guessed = 0
        for i in range(0, len(self._state)):
            log.debug(f"Compare {guess} == {self._state[i][0]}")
            if self._state[i][0] == guess:
                self._state[i][1] = True
                matched = True

            if self._state[i][1]:
                num_guessed = num_guessed + 1

        log.debug(f"Guessed {num_guessed}/{len(self._state)}")
        if num_guessed == len(self._state):
            log.debug("Game won")
            #     # Game won!
            self.end_game(True)
            return

        if not matched:
            self._guesses = self._guesses + 1
            print(
                f"Incorrect! You have {MAX_GUESSES - self._guesses} guesses remaining"
            )

        if self._guesses >= MAX_GUESSES:
            self.end_game(False)
            return

    def _reveal(self):
        log.debug("Revealing word")
        for i in range(0, len(self._state)):
            self._state[i][1] = True

    def choose(self):
        log.debug("Choosing word from set", num_words=self.num)
        try:
            i = randint(0, self.num)
            chosen = self.words[i].lower()
        except IndexError as e:
            log.error("Bad index when choosing word", ex=e, index=i, num_words=self.num)
            return ""

        # Create initial state
        self._state = [[c, False] for c in list(chosen)]
        log.debug(self._state)

        log.debug("Chosen word", word=chosen)
        return chosen

    def print_display(self):
        print(f"\n{self.display()}")

    def display(self):
        if self.chosen == "":
            log.error("No word chosen")
            return ""
        chars = []

        for c, visible in self._state:
            log.debug(f"{c} -> {visible}")
            if visible:
                chars.append(c)
            else:
                chars.append(BLANK)

        guessed = ",".join([v for v in self._guessed.keys()])

        message = f"[{guessed}]"
        if CHEAT:
            message = f"  {message} [Cheating: {self.chosen}]"
        if not self.running:
            message = "  Game over!"

        d = ".".join(chars)
        return f"{self._gibbet()}\n\n{d}{message}\n"

    def _gibbet(self):
        log.debug("Build gibbet")
        bits = MAN_BITS
        gib = list(ASSCII_GIBBET)

        for g in range(0, self._guesses):
            limb = bits[g]
            gib[limb[1]] = limb[0]

        return "".join(gib)
