from collections import deque

N, M, C = map(int, input().split())
graph = [[] for _ in range(N)]
trails = []

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in range(C):
    i, f, p = map(int, input().split())
    trails.append((i, f, p))

minTraces = [None] * N
def bfs(init):
    distance = [-1] * N
    distance[init] = 1
    q = deque([init])

    while q:
        node = q.popleft()
        for neig in graph[node]:
            if distance[neig] == -1:
                distance[neig] = distance[node] + 1
                q.append(neig)
    return distance



for i, f, m in trails:
    if minTraces[i] is None:
        minTraces[i] = bfs(i)
    d = minTraces[i][f]
    if d == -1 or d > m:
        print("MON TOYA POR FAVOR")
    else:
        print(d)