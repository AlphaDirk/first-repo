import numpy as np

grid = [[4,0,5,0,9,0,0,0,0],
        [0,6,0,8,0,0,0,2,0],
        [0,0,0,7,3,4,0,0,0],
        [0,5,7,9,4,6,0,3,0],
        [2,0,0,5,0,0,0,0,6],
        [0,0,6,0,0,0,0,4,5],
        [8,0,0,0,0,0,2,0,7],
        [0,7,0,3,0,1,0,8,4],
        [0,0,0,0,0,0,6,0,0]]

#At pos x, y, can n be place there
def possible(x,y,n):
    global grid
    for i in range(0, 9):
        if grid[i][y] == n:
            return False
    for j in range(0, 9):
        if grid[x][j] == n:
            return False
        
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0+i][y0+j] == n:
                return False
            
    return True
def total_zeros():
    global grid
    total = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if grid[i][j] == 0:
                total += 1
    return total

def solve():
    global grid
    while total_zeros() > 0:
        for i in range(0, 9):
            for j in range(0, 9):
                if grid[i][j] != 0:
                    continue
                poss_nums = []
                for k in range(1, 10):
                    if possible(i,j,k):
                        poss_nums.append(k)
                if len(poss_nums) != 1:
                    continue
                grid[i][j] = poss_nums[0]

    print(np.matrix(grid))
    return

solve()

"""
        [[4,0,5,0,9,0,0,0,0],
        [0,6,0,8,0,0,0,2,0],
        [0,0,0,7,3,4,0,0,0],
        [0,5,7,9,4,6,0,3,0],
        [2,0,0,5,0,0,0,0,6],
        [0,0,6,0,0,0,0,4,5],
        [8,0,0,0,0,0,2,0,7],
        [0,7,0,3,0,1,0,8,4],
        [0,0,0,0,0,0,6,0,0]]
        

"""