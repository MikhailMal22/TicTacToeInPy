import random
import time

winList = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]  ##all of the possible win combinations
board = [" "," "," "," "," "," "," "," "," "]                                ##array representing the game board
PLR = "X"
COM = "O"

##This function prints out game board
def printBoard():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def plrMove():
    while True:
        spot = input("Where will you place an X (1-9)?")
        if not spot.isdigit():
            print("Please enter a number")
        elif int(spot) > 9 or int(spot) < 1:
            print("Number must be between 1 and 9")
        elif board[int(spot)-1] == PLR or board[int(spot)-1] == COM:
            print("This spot is already taken")
        else:
            board[int(spot)-1] = PLR
            break

def comMove():
    while True:
        i = random.randint(0,8)
        if board[i] != PLR and board[i] != COM:
            board[i] = COM
            break

def checkIfWin(s):
    for subList in winList:
        if board[subList[0]] == s and board[subList[1]] == s and board[subList[2]] == s:
            if s == PLR:
                print("You win!")
            else:
                print("You lose!")
            printBoard()
            return True

    else:
        return False

def playAgain(g):
    answer = input("Play Again?(y/n)")
    if answer == "n":
        g = False
    else:
        g = True
        for i in range(len(board)):
            board[i] = " "
    return g

def changePlayer(p):
    if p == PLR:
        r = COM
        return r
    else:
        r = PLR
        return r


def main():
    game = True
    currentPlr = PLR
    spotsAvailable = 9
    while game == True:
        printBoard()
        time.sleep(0.5)

        if currentPlr == PLR:
            print("Your Turn!")
            plrMove()
            spotsAvailable -= 1

        if currentPlr == COM:
            print("Computer's turn!")
            comMove()
            spotsAvailable -= 1

        if checkIfWin(currentPlr):
            game = playAgain(game)
            spotsAvailable = 9

        if spotsAvailable <= 0:
            print("Draw")
            printBoard()
            game = playAgain(game)
            spotsAvailable = 9

        currentPlr = changePlayer(currentPlr)

main()