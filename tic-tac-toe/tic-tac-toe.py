import time


def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    welcome()
    printGrid(board)
    choice()


def choice():
    choice = int(input("Plesse enter where you would like to"
                 "make your move [1-9]\n"))
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
    time.sleep(3)


if __name__ == "__main__":
    main()
