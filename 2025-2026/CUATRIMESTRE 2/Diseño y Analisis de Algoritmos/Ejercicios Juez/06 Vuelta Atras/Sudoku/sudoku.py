grid = [list(map(int, input().split())) for _ in range(9)]

def is_feasible(grid, r, c, v):
    for i in range(9):
        if grid[r][i] == v:
            return False
        if grid[i][c] == v:
            return False
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == v:
                return False
    return True

def sudoku_bt(grid, k):
    if k == 81:
        return True
    r = k // 9
    c = k % 9
    if grid[r][c] != 0:
        return sudoku_bt(grid, k + 1)
    for v in range(1, 10):
        if is_feasible(grid, r, c, v):
            grid[r][c] = v
            if sudoku_bt(grid, k + 1):
                return True
            grid[r][c] = 0
    return False

sudoku_bt(grid, 0)
for row in grid:
    print(*row)