from time import sleep

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

count = 0

# algo to use fns and backtrack
def solve(grid):

    # counter to track iterations and visualize backtracking
    global count
    count += 1
    sleep(0.05)
    print('\nIteration: ' + str(count))
    print_sudoku(grid)

    # base case of recursion: board is full, that solution is found
    find = find_empty(grid)
    if not find:
        print("---------------------- ")
        print("  ^ Sudoku Solved ^")
        print("---------------------- ")
        return True
    else: 
        row, col = find

    # loop through values 1 - 9 to attempt to find solution
    for i in range(1, 10): # 1-9 inclusive

        # is plugging in 1-9 valid into board?
        if valid(grid, i, (row, col)): #(row, col) bc this is pos we found to be empty
        # yes? plug in the value
            grid[row][col] = i

            # try to finish the solution 
            if solve(grid): 
                return True
            
            #  if none of values work, reset to 0 to trigger find empty again [backtracking] 
            grid[row][col] = 0

    return False



def valid(grid, num, pos):
    
    # check row by looping through all cols in row
    for i in range(len(grid[0])):
        # checking each element (col) in the row [0] to see if it is the same as the num we just added in
            #  & if position we are checking is the position we just inserted something into, ignore
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # check col 
    for i in range(len(grid)):
        # checking each element (row) in the col to see if it is the same as the num we just added in
            #  & if position we are checking is the position we just inserted something into, ignore
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # check 3x3 square
    # determine which box we're in with integer (floor) division, will return 0 1 or 2
    box_y = pos[0] // 3
    box_x = pos[1] // 3

    # now that we know what box we're in, loop through 9 elements of the box
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True


def print_sudoku(grid):
    # for each [row] in the grid 
    for i in range(len(grid)):
        # print a horizontal line every three rows 
        if i % 3 == 0 and i != 0: 
            print ("----------------------")
    
        # for every position in the row
        for j in range(len(grid[0])):

            # print a vertical line every 3 elements
            if j % 3 == 0 and j != 0:
                print ("| ", end = "")

            if j == 8:
                print(grid[i][j])
            else: 
                print(str(grid[i][j]) + " ", end = "")


def find_empty(grid):
    # loop through board, find an empty spot denoted by 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j) # row, col position (y, x)

    return None


# print_sudoku(board)
solve(board)
# print_sudoku(board)