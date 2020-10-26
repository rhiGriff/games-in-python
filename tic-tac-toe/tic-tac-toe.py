import time

from itertools import cycle


def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    welcome()
    turn = cycle([1, 2])
    gameInPlay = True

    while gameInPlay:
        player = next(turn)
        if player == 1:
            letter = "O"
        else:
            letter = "X"
        printGrid(board)
        move = getPlayerMove(player, board, letter)
        print(move)


def getPlayerMove(player, board, letter):
    choice = None

    while True:
        try:
            choice = int(input(f"Player {player}: Please enter where you would like to"
                               f" place an {letter} [1-9]\n"))
        except ValueError:
            print("You must enter a number between 1 and 9\n")
            continue

        if not (1 <= choice <= 9):
            print("Your choice must be between 1 and 9\n")
            continue

        if not board[choice-1] == " ":
            print("That position has already been filled.  Please choose another\n")
            continue
        else:
            break

    return choice


# Prints a blank grid at the start of a game.
def printGrid(board):
    print(" %c | %c | %c " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[6], board[7], board[8]))
    print("   |   |   ")


def welcome():
    print("Welcome to Tic-Tac-Toe")
    print("Player1 is: O")
    print("Player2 is: X\n")
    print("Loading. Please wait...\n\n")
    time.sleep(1)


if __name__ == "__main__":
    main()
