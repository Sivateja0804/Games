player="x"
opponent="o"
import math
import time
def calculate_reward(board):
    #check all elements in the rows are equal
    for i in range(len(board)):
        if all(elem==player for elem in board[i]):
            return 10
        elif all(elem==opponent for elem in board[i]):
            return -10

    # check all elements in the columns are equal
    for i in range(len(board[0])):
        if board[0][i]==board[1][i]==board[2][i]==player:
            return 10
        elif board[0][i]==board[1][i]==board[2][i]==opponent:
            return -10

    # check diagonal elements  in the columns are equal
    if board[0][0]==board[1][1]==board[2][2]==player:
        return 10
    if board[0][0]==board[1][1]==board[2][2]==opponent:
        return -10
    if board[0][2]==board[1][1]==board[2][0]==player:
        return 10
    if board[0][2]==board[1][1]==board[2][0]==opponent:
        return -10

    return 0

def check_legal_moves(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="_":
                return True
    return False

def minmax(board,depth,isMax):
    reward=calculate_reward(board)

    if reward==10:
        return 10-depth
    if reward==-10:
        return -10+depth

    if not check_legal_moves(board):
        return 0

    if isMax:
        bestVal = -math.inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "_":
                    board[i][j] = player
                    bestVal = max(bestVal, minmax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return bestVal
    else:
        bestVal=math.inf
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="_":
                    board[i][j]=opponent
                    bestVal=min(bestVal,minmax(board, depth+1, not isMax))
                    board[i][j]="_"
        return bestVal

def get_next_move(board):
    bestReward=-math.inf
    bestMove=(-1,-1)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="_":
                board[i][j]=player
                reward=minmax(board,0,False)
                board[i][j]="_"
                if reward>bestReward:
                    bestReward=reward
                    bestMove=(i,j)
    return bestMove

def get_input():
    try:
        x, y = input()
        if x not in ["0","1","2"] or y not in ["0","1","2"]:
            print("please enter correct format")
            print("select 00-22 ex 00 01 02 10 11 12 20 21 22")
            x, y = get_input()
    except:
        print("please enter correct format")
        print("select 00-22 ex 00 01 02 10 11 12 20 21 22")
        x,y=get_input()
    return int(x),int(y)

def print_board(board):
    for i in range(3):
        print(board[i])

def check_game_status(board):
    score=calculate_reward(board)
    if score==10:
        print("You Lost. Better Luck next time")
        return "GAME LOST"
    elif score==-10:
        print("You Won")
        return "GAME WON"
    if not check_legal_moves(board):
        print("Game draw...")
        return "GAME DRAW"
    return "CONTINUE"

def start_play():
    board = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]
    while(True):
        print_board(board)
        status=check_game_status(board)
        if status!="CONTINUE":
            break
        print("Its your Turn Make a move : select 00-22 ex 00 01 02 10 11 12 20 21 22")
        x,y= get_input()
        if board[x][y]!="_":
            print("please select an empty place")
            continue
        else:
            board[x][y]=opponent
            print_board(board)
            status=check_game_status(board)
            time.sleep(1)
            if status=="CONTINUE":
                print("Now its my turn")
                optimalMove=get_next_move(board)
                board[optimalMove[0]][optimalMove[1]] = player
            else:
                break


