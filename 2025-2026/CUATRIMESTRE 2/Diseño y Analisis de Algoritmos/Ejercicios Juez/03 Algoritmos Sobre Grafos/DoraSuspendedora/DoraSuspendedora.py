N, M = map(int, input().split())
graph = [[] for _ in range(N)]
orderList = [[-2 for _ in range(N)]for _ in range(N)] # -2 = por ahora no sabemos, solo miramos hijos directos en esta creación-1 = antes 0 a la vez +1 despues
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    orderList[u][v] = -1
    orderList[v][u] = +1
P = int(input())
inicioAFin = [set() for _ in range(N)]
ordenConsultas = []
for _ in range(P):
    i, f = map(int, input().split())
    inicioAFin[i].add(f)
    ordenConsultas.append([i,f])

visited = [False for _ in range(N)]
ordered = []
def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    ordered.append(u)

for u in range(N):
    if not visited[u]:
        dfs(u)
        for o in ordered:
            orderList[u][o] = -1
            orderList[o][u] = 1
        ordered = []
        visited = [False for _ in range(N)]

for p1,p2 in ordenConsultas:
    if p1 == p2:
        print("A LA VEZ")
    elif (orderList[p1][p2] == -1 and orderList[p2][p1] != -1) or (orderList[p2][p1] == 1 and orderList[p1][p2] != 1):
        print("ANTES")
    elif (orderList[p1][p2] == 1 and orderList[p2][p1] != 1) or (orderList[p2][p1] == -1 and orderList[p1][p2] != -1):
        print("DESPUES")

    elif orderList[p1][p2] == -2 and orderList[p2][p1] == -2:
        print("A LA VEZ")
