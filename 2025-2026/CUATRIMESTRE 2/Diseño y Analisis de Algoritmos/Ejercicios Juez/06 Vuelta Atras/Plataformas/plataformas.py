n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visitado = [[False] * m for _ in range(n)]
mejor = float('inf')

def dfs(r, c, turno):
    global mejor

    if r == n - 1 and c == m - 1:
        if turno < mejor:
            mejor = turno
        return

    falta = (n - 1 - r) + (m - 1 - c)
    if turno + falta >= mejor:
        return

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not visitado[nr][nc] and grid[nr][nc] >= turno + 1:
            visitado[nr][nc] = True
            dfs(nr, nc, turno + 1)
            visitado[nr][nc] = False

if grid[0][0] >= 1:
    visitado[0][0] = True
    dfs(0, 0, 1)
print(mejor if mejor != float('inf') else "NO HAY SALIDA")