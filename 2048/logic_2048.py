import random

def get_grid():
    board=[]
    for i in range(4):
        board.append([0]*4)
    generate_random_2(board)
    return board

def generate_random_2(board):
    r=random.randint(0,3)
    c=random.randint(0,3)

    while board[r][c]!=0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    board[r][c]=2

def move_left(board):
    return

def move_right(board):
    return

def move_up(board):
    return

def move_down(board):
    return

def check_game_status(board):
    return
