#!/usr/bin/python3

"""N-queens puzzle"""

import sys

def init_board(size):
    """Initialize an `size`x`size` sized chessboard with spaces."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [board_deepcopy(row) for row in board]
    return board

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == "Q":
                solution.append([row, col])
                break
    return solution

def xout(board, row, col):
    """X out spots on a chessboard where queens can't be placed."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

def recursive_solve(board, current_row, placed_queens, solutions):
    """Recursively solve an N-queens puzzle and collect solutions."""
    if placed_queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[current_row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[current_row][col] = "Q"
            xout(tmp_board, current_row, col)
            solutions = recursive_solve(tmp_board, current_row + 1,
                                        placed_queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(N)
    solutions = recursive_solve(board, 0, 0, [])
    
    for solution in solutions:
        print(solution)

