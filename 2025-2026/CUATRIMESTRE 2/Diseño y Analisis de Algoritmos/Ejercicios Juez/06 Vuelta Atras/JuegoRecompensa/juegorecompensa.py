n, r, p = map(int, input().split())

vecinos = [set() for _ in range(n)]
for _ in range(r):
    a, b = map(int, input().split())
    vecinos[a].add(b)
    vecinos[b].add(a)

color = [-1] * n

def colorear(v):
    if v == n:
        return True
    for c in range(p):
        if all(color[u] != c for u in vecinos[v]):
            color[v] = c
            if colorear(v + 1):
                return True
            color[v] = -1
    return False

colorear(0)

for c in range(p):
    recompensas = [v for v in range(n) if color[v] == c]
    linea = f"{c} -> "
    for x in recompensas:
        linea += f"{x} "
    print(linea)