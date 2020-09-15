# Sudoku solver
# Can only handle really easy ones currently
# where some empty boxes only have one possible value

import numpy as np

grid = [
    [5,0,0,0,8,6,0,0,1],
    [0,0,2,7,0,1,6,0,0],
    [0,7,1,0,0,0,2,5,0],
    [9,1,0,0,2,0,0,7,0],
    [3,0,0,1,4,5,0,0,6],
    [0,6,0,0,9,0,0,2,4],
    [0,5,3,0,0,0,4,6,0],
    [0,0,8,9,0,3,5,0,0],
    [2,0,0,5,1,0,0,0,7]
    ]

# Creates a 3x3 box around grid[x][y]
def box_possible(x,y):
    if x % 3 == 0:
        box = []
        box.append(grid[x][y])
        box.append(grid[x+1][y])
        box.append(grid[x+2][y])
        if y % 3 == 0:
            box.append(grid[x][y+1])
            box.append(grid[x+1][y+1])
            box.append(grid[x+2][y+1])
            box.append(grid[x][y+2])
            box.append(grid[x+1][y+2])
            box.append(grid[x+2][y+2])
        elif y % 3 == 1:
            box.append(grid[x][y-1])
            box.append(grid[x+1][y-1])
            box.append(grid[x+2][y-1])
            box.append(grid[x][y+1])
            box.append(grid[x+1][y+1])
            box.append(grid[x+2][y+1])
        elif y % 3 == 2:
            box.append(grid[x][y-1])
            box.append(grid[x+1][y-1])
            box.append(grid[x+2][y-1])
            box.append(grid[x][y-2])
            box.append(grid[x+1][y-2])
            box.append(grid[x+2][y-2])
    elif x % 3 == 1:
        box = []
        box.append(grid[x][y])
        box.append(grid[x-1][y])
        box.append(grid[x+1][y])
        if y % 3 == 0:
            box.append(grid[x][y+1])
            box.append(grid[x-1][y+1])
            box.append(grid[x+1][y+1])
            box.append(grid[x][y+2])
            box.append(grid[x-1][y+2])
            box.append(grid[x+1][y+2])
        elif y % 3 == 1:
            box.append(grid[x][y-1])
            box.append(grid[x-1][y-1])
            box.append(grid[x+1][y-1])
            box.append(grid[x][y+1])
            box.append(grid[x-1][y+1])
            box.append(grid[x+1][y+1])
        elif y % 3 == 2:
            box.append(grid[x][y-1])
            box.append(grid[x-1][y-1])
            box.append(grid[x+1][y-1])
            box.append(grid[x][y-2])
            box.append(grid[x-1][y-2])
            box.append(grid[x+1][y-2])
    elif x % 3 == 2:
        box = []
        box.append(grid[x][y])
        box.append(grid[x-1][y])
        box.append(grid[x-2][y])
        if y % 3 == 0:
            box.append(grid[x][y+1])
            box.append(grid[x-1][y+1])
            box.append(grid[x-2][y+1])
            box.append(grid[x][y+2])
            box.append(grid[x-1][y+2])
            box.append(grid[x-2][y+2])
        elif y % 3 == 1:
            box.append(grid[x][y-1])
            box.append(grid[x-1][y-1])
            box.append(grid[x-2][y-1])
            box.append(grid[x][y+1])
            box.append(grid[x-1][y+1])
            box.append(grid[x-2][y+1])
        elif y % 3 == 2:
            box.append(grid[x][y-1])
            box.append(grid[x-1][y-1])
            box.append(grid[x-2][y-1])
            box.append(grid[x][y-2])
            box.append(grid[x-1][y-2])
            box.append(grid[x-2][y-2])
    return box

def possible(x,y,n):
    """ Finds the possible numbers for each box (if any) """

    # Makes sure box is empty
    if grid[x][y] == 0:
        
        # Checks column and row for same numbers
        for i in range(9):
            if grid[x][i] == n or grid[i][y] == n:
                return False

        # Checks 3x3 box for same numbers
        box = box_possible(x,y)
        if n in box:
            return False
        
    else:
        return False


# Main 
def main():    
    """ Prints out all the numbers for empty boxes """
    
    # Adds all possible values for a box to a list
    # Inputs the possible value if box can only be one value
    for j in range(9):
        for k in range(9):
            possible_list = []
            for i in range(1, 10):
                if possible(j,k,i) != False:
                     possible_list.append(i)
            if len(possible_list) == 1:
                grid[j][k] = possible_list[0]

    # Creates a grid after a solve and inputs all values on new grid as one list
    grid_after = []
    for j in range(9):
        for k in range(9):
            grid_after.append(grid[j][k])

    # Prints grid in matrix form
    print(np.matrix(grid))
    
    # Keep solving until there are no more zeroes
    if 0 in grid_after:
        main()


main()








                

                

                

