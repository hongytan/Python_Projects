# Sudoku solver using recursion

import pygame
import numpy as np

grid = [
    [0,1,0,0,5,0,0,9,0],
    [0,0,6,9,2,0,0,0,5],
    [0,5,0,0,0,4,0,6,0],
    [0,8,5,0,0,0,0,0,0],
    [0,0,9,7,0,6,8,0,0],
    [0,0,0,0,0,0,2,7,0],
    [0,9,0,5,0,0,0,8,0],
    [5,0,0,0,8,1,9,0,0],
    [0,3,0,0,9,0,0,2,0],
    ]

def possible(x,y,n):
    """ Finds the possible numbers for each box (if any) """
    
    # Checks column and row for same numbers
    for i in range(9):
        if grid[x][i] == n or grid[i][y] == n:
            return False

    # Checks 3x3 box for same numbers
    x0 = (x) // 3 * 3
    y0 = (y) // 3 * 3

    for i in range(3):
        for j in range(3):
            if grid[x0 + i][y0 + j] == n:
                return False
    
    return True


# Solves the sudoku puzzle 
def solve():    
    """ Prints out all the numbers for empty boxes """
    
    # Adds all possible values for a box to a list
    for j in range(9):
        for k in range(9):
            if grid[j][k] == 0:
                for i in range(1, 10):
                    if possible(j,k,i):
                        grid[j][k] = i
                        solve()
                        grid[j][k] = 0
                        
                return
            
    print(np.matrix(grid))

solve()
    
