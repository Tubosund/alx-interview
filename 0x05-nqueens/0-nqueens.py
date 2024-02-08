#!/usr/bin/python3
"""nqueen"""

import sys

def is_attacking(queens, row, col):
    """
    Checks if a queen at (row, col) attacks any existing queens.
    """
    for r, c in queens:
        if r == row or c == col or abs(r - row) == abs(c - col):
            return True
    return False

def solve_n_queens(n, queens=[]):
    """
    Recursively solves the N-Queens puzzle.
    """
    if len(queens) == n:
        # Print the solution
        print(*queens, sep=',')
        return

    for col in range(n):
        if not is_attacking(queens, len(queens), col):
            solve_n_queens(n, queens + [(len(queens), col)])

def main():
    """
    Handles program arguments and calls the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    solve_n_queens(n)

if __name__ == "__main__":
    main()
