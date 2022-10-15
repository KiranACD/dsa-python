# @param A : list of list of chars
def solveSudoku(A):

    for i in range(len(A)):
        A[i] = list(A[i])
    
    rows = [[False for j in range(9)] for i in range(9)]
    columns = [[False for j in range(9)] for i in range(9)]
    grids = [[False for j in range(9)] for i in range(9)]
    
    for i in range(9):
        for j in range(9):
            if A[i][j] == '.':
                continue
            else:
                num = int(A[i][j])
                rows[i][num-1] = True
                columns[j][num-1] = True
                grid = (i//3)*3 + (j//3)
                grids[grid][num-1] = True

    def is_safe(row, col, num, rows, columns, grids):
        grid = (row//3)*3 + (col//3)
        if (rows[row][num-1]) or (columns[col][num-1]) or (grids[grid][num-1]):
            return False
        rows[row][num-1] = True
        columns[col][num-1] = True
        grids[grid][num-1] = True
        return True
    
    def fill_sudoku(A, n, rows, columns, grids): 
        for row in range(n):
            for col in range(n):
                if A[row][col] != '.':
                    print('row: ', row)
                    print('col: ', col)
                    print('---------------------------------------')
                    continue
                for i in range(1, 10):
                    grid = (row//3)*3 + (col//3)
                    if is_safe(row, col, i, rows, columns, grids):
                        A[row][col] = i
                        if fill_sudoku(A, n, rows, columns, grids):
                            return True
                        A[row][col] = '.'
                        rows[row][i-1] = False
                        columns[col][i-1] = False
                        grids[grid][i-1] = False
                return False
        return True
            
    fill_sudoku(A, 9, rows, columns, grids)
    return A

A = [[5,3,'.','.',7,'.','.','.','.'], [6,'.','.',1,9,5,'.','.','.'], ['.',9,8,'.','.','.','.',6,'.'], [8,'.','.','.',6,'.','.','.',3], [4,'.','.',8,'.',3,'.','.',1], [7,'.','.','.','2','.','.','.',6], ['.',6,'.','.','.','.',2,8,'.'], ['.','.','.',4,1,9,'.','.',5], ['.','.','.','.',8,'.','.',7,9]]
A = solveSudoku(A)
print(A)