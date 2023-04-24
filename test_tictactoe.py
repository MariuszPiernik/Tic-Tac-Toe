from tictactoe import (
    winner,
    player,
    minimax,
    actions,
    result,
    terminal,
    utility,
)
import pytest

X = "X"
O = "O"
EMPTY = None


def main():
    test_player()
    test_actions()
    test_result()
    test_winner()
    test_terminal()
    test_utility()
    test_minimax()


def test_player():
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert player(board) == X
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [X, EMPTY, EMPTY]]
    assert player(board) == O
    board = [[EMPTY, X, O], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert player(board) == X
    board = [[EMPTY, X, EMPTY], [O, EMPTY, X], [EMPTY, EMPTY, EMPTY]]
    assert player(board) == O

def test_actions():
    board = [[X, O, X], [O, X, O], [X, EMPTY, EMPTY]]
    assert actions(board) == {(2, 1), (2, 2)}
    board = [[X, O, X], [O, X, O], [X, O, EMPTY]]
    assert actions(board) == {(2, 2)}
    board = [[X, EMPTY, X], [EMPTY, X, EMPTY], [X, EMPTY, EMPTY]]
    assert actions(board) == {(0, 1), (1, 0), (1, 2), (2, 1), (2, 2)}


def test_result():
    board = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert result(board,(1,0)) == [[X, X, X], [O, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    board = [[X, O, O], [X, O, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert result(board,(2,2)) == [[X, O, O], [X, O, EMPTY], [EMPTY, EMPTY, X]]
    board = [[X, O, X], [EMPTY, X, O], [O, EMPTY, EMPTY]]
    assert result(board,(1,0)) == [[X, O, X], [X, X, O], [O, EMPTY, EMPTY]]


def test_winner():
    # X won by row
    board = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert winner(board) == X
    # O won by row
    board = [[O, O, O], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert winner(board) == O
    # X won by column
    board = [[O, X, X], [X, X, EMPTY], [EMPTY, X, EMPTY]]
    assert winner(board) == X
    # O won by column
    board = [[O, X, O], [EMPTY, X, EMPTY], [O, X, EMPTY]]
    assert winner(board) == X
    # O won by diagonal
    board = [[O, X, X], [EMPTY, O, EMPTY], [X, X, O]]
    assert winner(board) == O
    # X won by diagonal
    board = [[O, O, X], [EMPTY, X, EMPTY], [X, O, EMPTY]]
    assert winner(board) == X
    # No winner
    board = [[EMPTY, O, EMPTY], [EMPTY, X, EMPTY], [EMPTY, O, EMPTY]]
    assert winner(board) == None


def test_utility():
    # X won by row
    board = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert utility(board) == 1
    # O won by row
    board = [[O, O, O], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert utility(board) == -1
    # X won by column
    board = [[O, X, X], [X, X, EMPTY], [EMPTY, X, EMPTY]]
    assert utility(board) == 1
    # O won by column
    board = [[O, X, O], [EMPTY, X, EMPTY], [O, X, EMPTY]]
    assert utility(board) == 1
    # O won by diagonal
    board = [[O, X, X], [EMPTY, O, EMPTY], [X, X, O]]
    assert utility(board) == -1
    # X won by diagonal
    board = [[O, O, X], [EMPTY, X, EMPTY], [X, O, EMPTY]]
    assert utility(board) == 1
    # No winner
    board = [[EMPTY, O, EMPTY], [EMPTY, X, EMPTY], [EMPTY, O, EMPTY]]
    assert utility(board) == 0


def test_minimax():
    board = [[O, O, EMPTY], [O, X, X], [X, X, EMPTY]]
    assert minimax(board) == (0,2)


def test_terminal():
    # GAME not END
    board = [[X, O, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert terminal(board) == False
    # X won  by row
    board = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    assert terminal(board) == True
    # O won by row
    board = [[EMPTY, EMPTY, EMPTY], [O, O, O], [EMPTY, EMPTY, EMPTY]]
    assert terminal(board) == True
    # X won by column
    board = [[EMPTY, EMPTY, X], [EMPTY, EMPTY, X], [EMPTY, EMPTY, X]]
    assert terminal(board) == True
    # O won by column
    board = [[EMPTY, O, EMPTY], [EMPTY, O, EMPTY], [EMPTY, O, EMPTY]]
    assert terminal(board) == True
    # X won by diagonal
    board = [[X, O, EMPTY], [O, X, EMPTY], [EMPTY, O, X]]
    assert terminal(board) == True
    # O won by diagonal
    board = [[O, X, O], [EMPTY, O, X], [O, X, EMPTY]]
    assert terminal(board) == True
    # Tie
    board = [[O, X, O], [O, X, X], [X, O, O]]
    assert terminal(board) == True


if __name__ == "__main__":
    main()
