from collections import deque

KN = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
META = (n - 1, m - 1)


dist = [[INF] * m for _ in range(n)]
if grid[META[0]][META[1]] != -1:
    dq = deque([META]); dist[META[0]][META[1]] = 0
    while dq:
        r, c = dq.popleft()
        for dr, dc in KN:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != -1 and dist[nr][nc] == INF:
                dist[nr][nc] = dist[r][c] + 1
                dq.append((nr, nc))

visitado = [[False] * m for _ in range(n)]
seen = [[0] * m for _ in range(n)]
sello = 0
mejor_rec = -1
mejor_saltos = INF

def inundacion(r0, c0):
    global sello
    sello += 1
    dq = deque()
    for dr, dc in KN:
        nr, nc = r0 + dr, c0 + dc
        if 0 <= nr < n and 0 <= nc < m and not visitado[nr][nc] and grid[nr][nc] != -1 and seen[nr][nc] != sello:
            seen[nr][nc] = sello; dq.append((nr, nc))
    meta = False; rec = 0
    while dq:
        r, c = dq.popleft()
        if grid[r][c] == 1: rec += 1
        if (r, c) == META: meta = True
        for dr, dc in KN:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and not visitado[nr][nc] and grid[nr][nc] != -1 and seen[nr][nc] != sello:
                seen[nr][nc] = sello; dq.append((nr, nc))
    return meta, rec

def dfs(r, c, rec, saltos):
    global mejor_rec, mejor_saltos
    if (r, c) == META:
        if rec > mejor_rec or (rec == mejor_rec and saltos < mejor_saltos):
            mejor_rec, mejor_saltos = rec, saltos
        return
    if dist[r][c] == INF:
        return


    alcanza_meta, rec_alcanzables = inundacion(r, c)
    if not alcanza_meta:
        return
    cota = rec + rec_alcanzables
    if cota < mejor_rec:
        return
    if cota == mejor_rec and saltos + dist[r][c] >= mejor_saltos:
        return

    for dr, dc in KN:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and not visitado[nr][nc] and grid[nr][nc] != -1:
            visitado[nr][nc] = True
            dfs(nr, nc, rec + (1 if grid[nr][nc] == 1 else 0), saltos + 1)
            visitado[nr][nc] = False


if grid[0][0] != -1 and dist[0][0] != INF:
    visitado[0][0] = True
    dfs(0, 0, 1 if grid[0][0] == 1 else 0, 0)

if mejor_rec >= 0:
    print(f"Consigo {mejor_rec} recompensas en {mejor_saltos} saltos")
else:
    print("Cosigo 0 recompensas en 0 saltos")