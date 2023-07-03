#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is an nqueens module
    Author: Peter Ekwere

"""
import sys

value = sys.argv[1]
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
else:
    try:
        value = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if value < 4:
        print("N must be at least 4")
        sys.exit(1)

def solve_nqueens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    
    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col-row+i >= 0 and board[i][col-row+i] == 'Q':
                return False
            if col+row-i < n and board[i][col+row-i] == 'Q':
                return False
        return True
    
    backtrack(0)
    return solutions

n = 4
solutions = solve_nqueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()

