n,m,r = map(int,input().split())
breach = [[[]for _ in range(m)]for _ in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        breach[i][j] = row[j]

def cubre(row, col):
    celdas = {(row, col)}
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        for paso in range(1, r + 1):
            ni, nj = row + di * paso, col + dj * paso

            if 0 <= ni < n and 0 <= nj < m:
                if breach[ni][nj] == 0:
                    celdas.add((ni, nj))
                elif breach[ni][nj] == -1:
                    break
            else: break

    return celdas

def is_feasible(breach, row, col):
    return breach[row][col] == 0

def cota(row, cubiertas):
    congeladas = 0
    for i in range(row - r):
        for j in range(m):
            if breach[i][j] == 0 and (i, j) not in cubiertas:
                congeladas += 1
    suelo_sin_cubrir = len(suelo) - len(cubiertas)
    cubrible_max = (n - row) * (1 + 4 * r)
    capacidad = suelo_sin_cubrir - cubrible_max

    return max(congeladas, capacidad, 0) #me quedo con la mayor solo si es positiva, el 0 evita negativos


suelo = {(i, j) for i in range(n) for j in range(m) if breach[i][j] == 0}

mejor = len(suelo)

def defensa_bt(row, cubiertas):
    global mejor
    if cota(row, cubiertas) >= mejor:
        return
    if row == n:
        sin_cubrir = len(suelo - cubiertas)
        if sin_cubrir < mejor:
            mejor = sin_cubrir
        return

    defensa_bt(row + 1, cubiertas)
    for col in range(m):
        if is_feasible(breach, row, col):
            defensa_bt(row + 1, cubiertas | cubre(row, col)) # | une los conjuntos cubiertas + las celdas que devuelve cubre para la colocacion en esa row y col de un lanzahechizos

defensa_bt(0, set())
print(mejor)