
def magic_square(r, c):
    print(
        """ For a magic grid, it is 3 by 3 list, enter numbers from 1 to 9, if the sum of rows, columns and diagonals is equal then it is a magic square, """)
    magic_grid = []
    for i in range(0, m):
        magic_grid += [0]
    for i in range(0, m):
        magic_grid[i] = [0] * n
    for i in range(0, m):
        for j in range(0, n):
            print('entry in row: ', i + 1, ' column: ', j + 1, " = ")
            magic_grid[i][j] = int(input())
        print(magic_grid)
    for row in magic_grid:
        for col in row:
            print(col, end="  ")
        print()
    row = len(magic_grid)
    column = len(magic_grid[0])
    for i in range(0, row):
        sum_row = 0
        sum_col = 0
        for j in range(0, column):
            sum_row = sum_row + magic_grid[i][j]
            sum_col = sum_col + magic_grid[j][i]
        print("for row", i + 1, " : ", sum_row)
        print("for column", i + 1, " : ", sum_col)

    sum_left_diag = 0
    sum_right_diag = 0
    size = len(magic_grid)
    for i in range(size):
        for j in range(size):
            if i == j:
                sum_left_diag = sum_left_diag + magic_grid[i][i]
            if i + j == size - 1:
                sum_right_diag = sum_right_diag + magic_grid[i][j]
    print("for left diagonal ", sum_left_diag)
    print("for right diagonal ", sum_right_diag)
    if sum_row == sum_col == sum_left_diag == sum_right_diag:
        print("it is a magic grid")
    else:
        print("not a magic grid")


m = int(input('number of rows, r = '))
n = int(input('number of columns, c = '))
magic_square(r=m, c=n)
