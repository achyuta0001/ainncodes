board=["_","_","_",
    "_","_","_",
    "_","_","_",]
currp="X"
winner = None
gamerun=True

#print board

def printb(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])


#player input
def playeri(board):
    imp=int(input("enter number 0 to 8"))
    if imp>=0 and imp<=9 and board[imp]=="_":
        board[imp]=currp
    else:
        print("not possible") 
#check win
def checkwin(board):
    global winner
    if board[0]==board[1]==board[2]!="_":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5]!="_":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8]!="_":
        winner=board[7]
        return True
    elif board[0]==board[3]==board[6]!="_":
        winner=board[3]
        return True
    elif board[1]==board[4]==board[7]!="_":
        winner=board[4]
        return True
    elif board[2]==board[4]==board[8]!="_":
        winner=board[4]
        return True
    elif board[0]==board[5]==board[8]!="_":
        winner=board[5]
        return True
    elif board[2]==board[4]==board[6]!="_":
        winner=board[4]
        return True
def checktie(board):
    global gamerun
    if "_" not in  board:
        print(board)
        print("game tied")
        gamerun=False


def checkdone(board):
    if checkwin(board):
        print(f"the winner is {winner} ")
        gamerun=False
#switch player
def switchp():
    global currp
    if currp=="X":
        currp="O"
    else:
        currp="X"

while gamerun:
    printb(board)
    playeri(board)
    checkdone(board)
    checktie(board)
    switchp()