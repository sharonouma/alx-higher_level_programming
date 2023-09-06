#!/usr/bin/python3
"""
Queen class
"""

from sys import argv


class Queen:
    """
    Class to solve the N-Queens problem using recursion.
    """
    def __init__(self, N):
        """
        Initialize the Queen class with the board size N and an empty list for
        storing the right positions.
        """
        self.N = N
        self.right = [None] * N

    def can_move(self, x, y):
        """
        Check if a queen can be placed at position (x, y) without attacking
        any other queens.
        """
        for a in range(x):
            if self.right[a] == y or abs(self.right[a] - y) == (x - a):
                return False
        return True

    def solution(self, n):
        """
        Recursively find and print all possible solutions to the
        N-Queens problem.
        """
        if n == self.N:
            print([[j, self.right[j]] for j in range(self.N)])
            return

        for j in range(self.N):
            if self.can_move(n, j):
                self.right[n] = j
                self.solution(n + 1)


if __name__ == "__main__":
    count = len(argv)

    if count != 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            N = int(argv[1])
        except ValueError:
            print("N must be a number")
            exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    final = Queen(N)
    final.solution(0)
