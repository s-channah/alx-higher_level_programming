#!/usr/bin/python3

import sys


def is_safe(board, r, col, n):
    for i in range(col):
        if board[r][i] == 1:
            return False

    for i, j in zip(range(r, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(r, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve_util(col):
        if col == n:
            solutions.append([[i, r.index(1)] for i, r in enumerate(board)])
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve_util(col + 1)
                board[i][col] = 0

    solve_util(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
