player="x"
opponent="o"
import math
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



if __name__ == "__main__":

    board=[["_","_","_"],
           ["o","o","_"],
           ["x","_","_"]]

    optimalMove=get_next_move(board)
    print(optimalMove)


