import time

from itertools import cycle


class Board(object):

    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __str__(self):
        return "\n %c | %c | %c \n" \
               "___|___|___     \n" \
               " %c | %c | %c   \n" \
               "___|___|___     \n" \
               " %c | %c | %c   \n" \
               "   |   |        \n" \
               % (self.board[0], self.board[1], self.board[2],
                  self.board[3], self.board[4], self.board[5],
                  self.board[6], self.board[7], self.board[8])

    @property
    def diagonals(self):
        return [[self.board[0], self.board[4], self.board[8]],
                [self.board[2], self.board[4], self.board[6]]]

    @property
    def rows(self):
        return [[self.board[0], self.board[1], self.board[2]],
                [self.board[3], self.board[4], self.board[5]],
                [self.board[6], self.board[7], self.board[8]]]

    @property
    def columns(self):
        return [[self.board[0], self.board[3], self.board[6]],
                [self.board[1], self.board[4], self.board[7]],
                [self.board[2], self.board[5], self.board[8]]]


def main():
    board = Board()
    welcome()
    print(board)
    turn = cycle([1, 2])
    gameInPlay = True

    while gameInPlay:
        player = next(turn)
        if player == 1:
            letter = "O"
        else:
            letter = "X"
        move = getPlayerMove(player, board, letter)
        board.board[move-1] = letter
        print(board)
        if hasPlayerWon(board, letter):
            print(f"Player {player} wins!")
            break
        if " " not in board.board:
            print("It's a draw! Nobody wins :-(")
            break

    if input("Play again (Y/N)?\n").lower() == "y":
        main()
    else:
        exit()


def getPlayerMove(player, board, letter):
    choice = None

    while True:
        try:
            choice = int(input(f"Player {player}: Please enter where you would like to"
                               f" place an {letter} [1-9]:\n"))
        except ValueError:
            print("You must enter a number between 1 and 9.\n")
            continue

        if not (1 <= choice <= 9):
            print("Your choice must be between 1 and 9.\n")
            continue

        if board.board[choice-1] != " ":
            print("That position has already been filled.  Please choose another.\n")
            continue
        else:
            break

    return choice


def hasPlayerWon(board, letter):
    lines = board.rows + board.columns + board.diagonals

    for line in lines:
        if all(board_position == letter for board_position in line):
            return True


def welcome():
    print("Welcome to Tic-Tac-Toe")
    print("Player1 is: O")
    print("Player2 is: X\n")
    print("Loading. Please wait...\n\n")
    time.sleep(1)


if __name__ == "__main__":
    main()
