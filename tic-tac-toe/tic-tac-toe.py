import time

from itertools import cycle


def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    welcome()
    printGrid(board)
    turn = cycle([1, 2])
    gameInPlay = True

    while gameInPlay:
        player = next(turn)
        if player == 1:
            letter = "O"
        else:
            letter = "X"
        move = getPlayerMove(player, board, letter)
        board[move-1] = letter
        printGrid(board)
        if hasPlayerWon(board, letter):
            print(f"Player {player} wins!")
            exit()
        if " " not in board:
            print("It's a draw! Nobody wins :-(")
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

        if board[choice-1] != " ":
            print("That position has already been filled.  Please choose another.\n")
            continue
        else:
            break

    return choice


def hasPlayerWon(board, letter):
    return ((board[0] == letter and board[1] == letter and board[2] == letter) or
            (board[3] == letter and board[4] == letter and board[5] == letter) or
            (board[6] == letter and board[7] == letter and board[8] == letter) or
            (board[0] == letter and board[3] == letter and board[6] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[0] == letter and board[4] == letter and board[8] == letter) or
            (board[2] == letter and board[4] == letter and board[6] == letter))


# Prints a blank grid at the start of a game.
def printGrid(board):
    print("\n %c | %c | %c " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[6], board[7], board[8]))
    print("   |   |   \n")


def welcome():
    print("Welcome to Tic-Tac-Toe")
    print("Player1 is: O")
    print("Player2 is: X\n")
    print("Loading. Please wait...\n\n")
    time.sleep(1)


if __name__ == "__main__":
    main()
