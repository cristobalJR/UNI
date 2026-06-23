DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 0x3f3f3f3f

n, m = map(int, input().split())
grid = [input().split() for _ in range(n)]

for r in range(n):
    for c in range(m):
        if grid[r][c] == 'P': pr, pc = r, c
        elif grid[r][c] == 'V': vr, vc = r, c
        elif grid[r][c] == 'M': mr, mc = r, c
        elif grid[r][c] == 'C': cr, cc = r, c

def bfs(sr, sc):
    dist = [[INF] * m for _ in range(n)]
    dist[sr][sc] = 0
    cola = [(sr, sc)]
    cabeza = 0
    while cabeza < len(cola):
        r, c = cola[cabeza]
        cabeza += 1
        for d in DIRS:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 'W' and dist[nr][nc] == INF:
                dist[nr][nc] = dist[r][c] + 1
                cola.append((nr, nc))
    return dist

dM = bfs(mr, mc); dC = bfs(cr, cc); dV = bfs(vr, vc)
dMC = dM[cr][cc]
dMV = dM[vr][vc]
dCV = dC[vr][vc]

def cota(r, c, tiene_m, tiene_c):
    if tiene_m and tiene_c:
        return dV[r][c]
    if tiene_m:
        return dC[r][c] + dCV
    if tiene_c:
        return dM[r][c] + dMV
    return min(dM[r][c] + dMC + dCV, dC[r][c] + dMC + dMV)

visitado = [[False] * m for _ in range(n)]
mejor = INF

def bt(r, c, tiene_m, tiene_c, pasos):
    global mejor
    if pasos >= mejor:
        return
    if r == vr and c == vc:
        if tiene_m and tiene_c:
            mejor = pasos
        return
    if pasos + cota(r, c, tiene_m, tiene_c) >= mejor:
        return

    opciones = []
    for d in DIRS:
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 'W' and not visitado[nr][nc]:
            nm = tiene_m or grid[nr][nc] == 'M'
            ncoca = tiene_c or grid[nr][nc] == 'C'
            opciones.append([pasos + 1 + cota(nr, nc, nm, ncoca), nr, nc, nm, ncoca])
    opciones.sort()
    for op in opciones:
        nr = op[1]; nc = op[2]; nm = op[3]; ncoca = op[4]
        visitado[nr][nc] = True
        bt(nr, nc, nm, ncoca, pasos + 1)
        visitado[nr][nc] = False

visitado[pr][pc] = True
bt(pr, pc, False, False, 0)
print(mejor if mejor != INF else "Imposible")