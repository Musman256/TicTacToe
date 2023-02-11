import os
import time

GameBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
GameTrue = True
PlayerTurn = "X"

clearConsole = lambda: os.system("cls")

while GameTrue:
    clearConsole()
    
    if (GameBoard[0] == "X" and GameBoard[1] == "X" and GameBoard[2] == "X") or (GameBoard[3] == "X" and GameBoard[4] == "X" and GameBoard[5] == "X") or (GameBoard[6] == "X" and GameBoard[7] == "X" and GameBoard[8] == "X") or (GameBoard[0] == "X" and GameBoard[3] == "X" and GameBoard[6] == "X") or (GameBoard[1] == "X" and GameBoard[4] == "X" and GameBoard[7] == "X") or (GameBoard[2] == "X" and GameBoard[5] == "X" and GameBoard[8] == "X") or (GameBoard[0] == "X" and GameBoard[4] == "X" and GameBoard[8] == "X") or (GameBoard[2] == "X" and GameBoard[4] == "X" and GameBoard[6] == "X"):
        print("X is the winner!")
        GameTrue = False
    elif (GameBoard[0] == "O" and GameBoard[1] == "O" and GameBoard[2] == "O") or (GameBoard[3] == "O" and GameBoard[4] == "O" and GameBoard[5] == "O") or (GameBoard[6] == "O" and GameBoard[7] == "O" and GameBoard[8] == "O") or (GameBoard[0] == "O" and GameBoard[3] == "O" and GameBoard[6] == "O") or (GameBoard[1] == "O" and GameBoard[4] == "O" and GameBoard[7] == "O") or (GameBoard[2] == "O" and GameBoard[5] == "O" and GameBoard[8] == "O") or (GameBoard[0] == "O" and GameBoard[4] == "O" and GameBoard[8] == "O") or (GameBoard[2] == "O" and GameBoard[4] == "O" and GameBoard[6] == "O"):
        print("O is the winner!")
        GameTrue = False
    
    print(GameBoard[0] + "|" + GameBoard[1] + "|" + GameBoard[2] + "\n-+-+-")
    print(GameBoard[3] + "|" + GameBoard[4] + "|" + GameBoard[5] + "\n-+-+-")
    print(GameBoard[6] + "|" + GameBoard[7] + "|" + GameBoard[8])
    
    try:
        UserInput = int(input(f"\nEnter a position ({PlayerTurn}'s turn): "))
    except:
        print("Please enter a valid position (1-9).")
        time.sleep(2)
    
    if UserInput == 1 and GameBoard[0] == " " and PlayerTurn == "X":
        GameBoard[0] = "X"
        PlayerTurn = "O"
    elif UserInput == 2 and GameBoard[1] == " " and PlayerTurn == "X":
        GameBoard[1] = "X"
        PlayerTurn = "O"
    elif UserInput == 3 and GameBoard[2] == " " and PlayerTurn == "X":
        GameBoard[2] = "X"
        PlayerTurn = "O"
    elif UserInput == 4 and GameBoard[3] == " " and PlayerTurn == "X":
        GameBoard[3] = "X"
        PlayerTurn = "O"
    elif UserInput == 5 and GameBoard[4] == " " and PlayerTurn == "X":
        GameBoard[4] = "X"
        PlayerTurn = "O"
    elif UserInput == 6 and GameBoard[5] == " " and PlayerTurn == "X":
        GameBoard[5] = "X"
        PlayerTurn = "O"
    elif UserInput == 7 and GameBoard[6] == " " and PlayerTurn == "X":
        GameBoard[6] = "X"
        PlayerTurn = "O"
    elif UserInput == 8 and GameBoard[7] == " " and PlayerTurn == "X":
        GameBoard[7] = "X"
        PlayerTurn = "O"
    elif UserInput == 9 and GameBoard[8] == " " and PlayerTurn == "X":
        GameBoard[8] = "X"
        PlayerTurn = "O"
    elif UserInput == 1 and GameBoard[0] == " " and PlayerTurn == "O":
        GameBoard[0] = "O"
        PlayerTurn = "X"
    elif UserInput == 2 and GameBoard[1] == " " and PlayerTurn == "O":
        GameBoard[1] = "O"
        PlayerTurn = "X"
    elif UserInput == 3 and GameBoard[2] == " " and PlayerTurn == "O":
        GameBoard[2] = "O"
        PlayerTurn = "X"
    elif UserInput == 4 and GameBoard[3] == " " and PlayerTurn == "O":
        GameBoard[3] = "O"
        PlayerTurn = "X"
    elif UserInput == 5 and GameBoard[4] == " " and PlayerTurn == "O":
        GameBoard[4] = "O"
        PlayerTurn = "X"
    elif UserInput == 6 and GameBoard[5] == " " and PlayerTurn == "O":
        GameBoard[5] = "O"
        PlayerTurn = "X"
    elif UserInput == 7 and GameBoard[6] == " " and PlayerTurn == "O":
        GameBoard[6] = "O"
        PlayerTurn = "X"
    elif UserInput == 8 and GameBoard[7] == " " and PlayerTurn == "O":
        GameBoard[7] = "O"
        PlayerTurn = "X"
    elif UserInput == 9 and GameBoard[8] == " " and PlayerTurn == "O":
        GameBoard[8] = "O"
        PlayerTurn = "X"