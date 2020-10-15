def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    printGrid(board)


def printGrid(board):
    print(" %c | %c | %c " % (board[0], board[1], board[2]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[3], board[4], board[5]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[6], board[7], board[8]))
    print("   |   |   ")


if __name__ == "__main__":
    main()
