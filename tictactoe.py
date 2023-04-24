"""
Tic Tac Toe Player
"""
# ?
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return  [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]




def player(board):
    """
    Returns player who has the next turn on a board.
    """

    countX = 0
    countO = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO +=1
    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    allPossibleActions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                allPossibleActions.add((row,col))
    return allPossibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Not valid action')
    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checkRow(board,player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board,player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkFirstDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def checkSecondDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

"""
Returns the winner of the game, if there is one.
"""
def winner(board):
    if checkRow(board, X) or checkCol(board,X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    if checkRow(board, O) or checkCol(board,O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == O or winner(board) == X:
        return True
    for row in range(len(board)):
        for col  in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def vmin(board):
    value = math.inf
    if terminal(board):
        return utility(board)
    else:
        for action in actions(board):
            value = min(value, vmax(result(board, action)))
    return value


def vmax(board):
    value = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        value = max(value, vmin(result(board, action)))
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    moves = actions(board)

    if terminal(board):
        return None
    elif player(board) == O:
        options = []
        for move in moves:
            options.append([vmax(result(board, move)), move])
        return sorted(options, key=lambda x: x[0])[0][1]

    elif player(board) == X:
        options = []
        for move in moves:
            options.append([vmin(result(board, move)), move])
        return sorted(options, key=lambda x: x[0], reverse=True)[0][1]

