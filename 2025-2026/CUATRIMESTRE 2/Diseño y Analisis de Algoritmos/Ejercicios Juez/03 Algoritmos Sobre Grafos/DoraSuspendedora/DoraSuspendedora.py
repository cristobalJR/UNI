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