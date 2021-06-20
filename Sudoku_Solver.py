
def printMaze(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
        print()


def checkBox(grid, row, col, num):
    for i in range(row, row+3):
        for j in range(col, col+3):
            if grid[i][j] == num:
                return False
    return True


def checkRow(grid, row, num):
    for j in range(9):
        if grid[row][j] == num:
            return False
    return True


def checkCol(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return False
    return True


def checkSafe(grid, row, col, num):

    if checkRow(grid, row, num) and checkCol(grid, col, num) and checkBox(grid, 3*(row//3), 3*(col//3), num):
        return True
    return False


def isEmpty(grid, l):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                l[0], l[1] = i, j
                return True
    return False


def solveSudoku(maze):
    l = [0, 0]
    if isEmpty(maze, l):
        row = l[0]
        col = l[1]
    else:
        return True

    for num in range(1, 10):
        if checkSafe(maze, row, col, num):

            maze[row][col] = num

            if solveSudoku(maze):
                return True

        maze[row][col] = 0

    return False


sudoku_maze = [[3, 0, 0, 6, 1, 0, 0, 0, 8],
               [0, 0, 2, 0, 3, 0, 7, 6, 0],
               [0, 0, 0, 7, 5, 0, 2, 9, 0],
               [0, 9, 0, 8, 0, 0, 0, 1, 0],
               [0, 4, 0, 1, 7, 3, 0, 5, 0],
               [0, 5, 0, 0, 0, 9, 0, 2, 0],
               [0, 3, 7, 0, 4, 1, 0, 0, 0],
               [0, 2, 5, 0, 8, 0, 9, 0, 0],
               [4, 0, 0, 0, 9, 7, 0, 0, 2]]

if __name__ == '__main__':

    pass
