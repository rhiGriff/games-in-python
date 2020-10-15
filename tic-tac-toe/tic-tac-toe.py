import sys

BOARD = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def main(BOARD):
    printGrid(BOARD)

def printGrid(BOARD):
    print(" %c | %c | %c " % (BOARD[0],BOARD[1],BOARD[2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (BOARD[3],BOARD[4],BOARD[5]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (BOARD[6],BOARD[7],BOARD[8]))    
    print("   |   |   ")

if __name__ == "__main__":
    main(BOARD) 