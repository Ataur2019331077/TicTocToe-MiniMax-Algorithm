"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                count_X += 1
            elif board[i][j] == O:
                count_O += 1
    
    return X if count_X == count_O else O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x, y) = action

    if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
        raise IndexError
    
    new_board = [row[:] for row in board]
    new_board[x][y] = player(board)
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkPrincipleDiag(board, X) or checkOtherDiag(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkPrincipleDiag(board, O) or checkOtherDiag(board, O):
        return O
    return None

def checkRow(board, player):
    for i in range(len(board)):
        count = 0
        for j in range(len(board[0])):
            if board[i][j] == player:
                count += 1
        
        if count == 3:
            return True
    return False

def checkCol(board, player):
    for j in range(len(board[0])):
        count = 0
        for i in range(len(board)):
            if board[i][j] == player:
                count += 1
        if count == 3:
            return True
    return False

def checkPrincipleDiag(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    return False

def checkOtherDiag(board, player):
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def isTie(board):
    count = 9
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count -= 1

    return count == 0

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or isTie(board):
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        arr = []
        for action in actions(board):
            arr.append([min_val(result(board, action)), action])
        
        return sorted(arr, key=lambda x : x[0], reverse=True)[0][1]
    else:
        arr = []
        for action in actions(board):
            arr.append([max_val(result(board, action)), action])
        
        return sorted(arr, key=lambda x : x[0])[0][1]



def max_val(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    
    return v

def min_val(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    
    return v
