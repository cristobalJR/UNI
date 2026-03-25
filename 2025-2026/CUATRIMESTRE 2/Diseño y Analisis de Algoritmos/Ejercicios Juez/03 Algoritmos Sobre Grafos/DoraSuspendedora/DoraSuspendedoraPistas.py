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
print(graph)
print(orderList)
print(inicioAFin)
print(ordenConsultas)

def dfs(i,j):
    stack = [i]
    visited = [False for _ in range(N)]
    visited[i] = True
    while stack:
        u = stack.pop()
        if u == j:
            return True
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return False

for p1,p2 in ordenConsultas:
    if p1 == p2:
        print("A LA VEZ")
    elif orderList[p1][p2] == -1 and orderList[p2][p1] != -1:
        print("ANTES")
    elif orderList[p1][p2] == 1 and orderList[p2][p1] != 1:
        print("DESPUES")
    else:
        r1 = dfs(p1,p2)
        r2 = dfs(p2,p1)
        if r1 and not r2:
            print("ANTES")
        elif r2 and not r1:
            print("DESPUES")
        else:
            print("A LA VEZ")