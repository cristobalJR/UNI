N, M, P = input().split()
N = int(N)
M = int(M)

saga = []
for _ in range(N):
    saga.append(input().strip())

gente = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    if saga[a] == P and saga[b] == P:
        gente[a].append(b)
        gente[b].append(a)

visitado = [False] * N
salas = 0

def dfs(u):
    visitado[u] = True
    for v in gente[u]:
        if not visitado[v]:
            dfs(v)

for i in range(N):
    if saga[i] == P and not visitado[i]:
        salas += 1
        dfs(i)

print(salas)

