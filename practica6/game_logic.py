# game_logic.py

import numpy as np

ROWS = 6
COLS = 7

def create_board():
    return np.zeros((ROWS, COLS))

def drop_piece(board, col, piece):
    for row in reversed(range(ROWS)):
        if board[row][col] == 0:
            board[row][col] = piece
            return True
    return False

def is_valid_location(board, col):
    return board[0][col] == 0

def get_valid_locations(board):
    return [c for c in range(COLS) if is_valid_location(board, c)]

def check_win(board, piece):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False