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

trailsPorOrigen = [[] for _ in range(N)]

for index in range(C):
    i, f, p = trails[index]
    trailsPorOrigen[i].append((f, p, index))
answers = [""] * C

def bfs(init, trailsDelOrigen):
    distance = [-1] * N
    distance[init] = 1

    maxP = 0
    objetivos = [False] * N
    objetivosDistintos = 0

    for f, p, _ in trailsDelOrigen:
        if p > maxP:
            maxP = p
        if not objetivos[f]:
            objetivos[f] = True
            objetivosDistintos += 1

    encontrados = 0
    if objetivos[init]:
        encontrados = 1

    q = deque([init])
    while q and encontrados < objetivosDistintos:
        node = q.popleft()
        siguiente = distance[node] + 1

        if siguiente > maxP:
            continue

        for neig in graph[node]:
            if distance[neig] == -1:
                distance[neig] = siguiente

                if objetivos[neig]:
                    encontrados += 1

                q.append(neig)
    return distance

for i in range(N):
    if trailsPorOrigen[i]:
        distance = bfs(i, trailsPorOrigen[i])

        for f, p, index in trailsPorOrigen[i]:
            d = distance[f]
            if d != -1 and d <= p:
                answers[index] = str(d)
            else:
                answers[index] = "MON TOYA POR FAVOR"

for ans in answers:
    print(ans)