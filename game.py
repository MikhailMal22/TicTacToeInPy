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

def plrMove(available,XList):
    while True:
        spot = input("Where will you place an X (1-9)?")
        if not spot.isdigit():
            print("Please enter a number")
        elif int(spot) > 9 or int(spot) < 1:
            print("Number must be between 1 and 9")
        elif board[int(spot)-1] == PLR or board[int(spot)-1] == COM:
            print("This spot is already taken")
        else:
            spotInt = int(spot)-1
            board[spotInt] = PLR
            XList.append(spotInt)
            available.remove(spotInt)
            break

def comPlace(list,available,i):
    board[i] = COM
    list.append(i)
    available.remove(i)

def comMove(available,OList,XList):

    if len(available) > 1 and len(available) < 9:
        candidate = 0
        if len(XList) > 1:
            #print("Xlist is bigger than one, looking for a winList")
            k = XList[-1]
            j = XList[-2]
            for list in winList:
                if k in list and j in list:
                    candidate = list
                    #print(f"found potential candidate:{candidate}")
                    break
            if candidate != 0:
                for num in candidate:
                    if num != k and num != j and num in available:
                        i = num
                        comPlace(OList,available,i)
                        break
                else:
                    candidate = 0

        if candidate == 0:
            #print("either list is size one or candidate wasnt found")
            j = XList[-1]
            for list in winList:
                if j in list:
                    candidate = list
                    #print(f"found potential candidate {candidate}")
                    for num in candidate:
                        if num != j and num in available:
                            i = num
                            comPlace(OList,available,i)
                            break
                    else:
                        continue
                    break

    elif len(available) == 9:
        #print("all spots in the board are available")
        i = random.randint(0,8)
        comPlace(OList,available,i)

    elif len(available) == 1:
        #print("one spot left")
        i = available[0]
        comPlace(OList,available,i)

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
    available = [0,1,2,3,4,5,6,7,8]
    XList = []
    OList = []
    while game == True:
        printBoard()
        time.sleep(0.5)

        if currentPlr == PLR:
            print("Your Turn!")
            plrMove(available,XList)
            spotsAvailable -= 1

        if currentPlr == COM:
            print("Computer's turn!")
            comMove(available,OList,XList)
            spotsAvailable -= 1

        if checkIfWin(currentPlr):
            game = playAgain(game)
            spotsAvailable = 9
            available = [0,1,2,3,4,5,6,7,8]
            XList = []
            OList = []

        if spotsAvailable <= 0:
            print("Draw")
            printBoard()
            game = playAgain(game)
            spotsAvailable = 9
            available = [0,1,2,3,4,5,6,7,8]
            XList = []
            OList = []

        currentPlr = changePlayer(currentPlr)

main()