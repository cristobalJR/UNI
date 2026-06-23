n = int(input().split()[0])
grid = [list(map(int, input().split())) for _ in range(n)]
fi, ci, ff, cf = map(int, input().split())

num = [[-1] * n for _ in range(n)]
total = 0
for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            num[r][c] = total
            total = total + 1

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = 0x3f3f3f3f
cogido = [False] * total
mejor = INF
visto = {}

def sonic_bt(r, c, n_cog, tiempo):
    global mejor
    if tiempo >= mejor:
        return
    if r == ff and c == cf and n_cog == total:
        mejor = tiempo
        return

    s = ""
    for x in cogido:
        if x:
            s = s + "1"
        else:
            s = s + "0"
    clave = str(r) + "," + str(c) + "," + s
    if clave in visto and visto[clave] <= tiempo:
        return
    visto[clave] = tiempo

    for d in DIRS:
        dr = d[0]
        dc = d[1]
        rr = r
        cc = c
        pasos = 0
        nuevos = []
        nr = rr + dr
        nc = cc + dc
        while 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 3:
            rr = nr
            cc = nc
            pasos = pasos + 1
            if grid[rr][cc] == 1 and not cogido[num[rr][cc]]:
                cogido[num[rr][cc]] = True
                nuevos.append(num[rr][cc])
            nr = rr + dr
            nc = cc + dc
        if pasos > 0:
            sonic_bt(rr, cc, n_cog + len(nuevos), tiempo + pasos)
        for i in nuevos:
            cogido[i] = False

inicio = 0
if grid[fi][ci] == 1:
    cogido[num[fi][ci]] = True
    inicio = 1
sonic_bt(fi, ci, inicio, 1)

print(mejor if mejor != INF else -1)