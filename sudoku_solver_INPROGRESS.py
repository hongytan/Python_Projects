# Sudoku solver

grid = [
    [0,8,0,0,0,0,2,0,0],
    [0,0,0,0,8,4,0,9,0],
    [0,0,6,3,2,0,0,1,0],
    [0,9,7,0,0,0,0,8,0],
    [8,0,0,9,0,3,0,0,2],
    [0,1,0,0,0,0,9,5,0],
    [0,7,0,0,4,5,8,0,0],
    [0,3,0,7,1,0,0,0,0],
    [0,0,8,0,0,0,0,4,0]
    ]

def create_box(r1,c1):
    box = []
    box.append(grid[r1][c1:c1+3])
    box.append(grid[r1+1][c1:c1+3])
    box.append(grid[r1+2][c1:c1+3])
    return box

box_1 = create_box(0,0)
box_2 = create_box(0,3)
box_3 = create_box(0,6)
box_4 = create_box(3,0)
box_5 = create_box(3,3)
box_6 = create_box(3,6)
box_7 = create_box(6,0)
box_8 = create_box(6,3)
box_9 = create_box(6,6)

print(box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9)




                

                

