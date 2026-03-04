N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start, end = map(int, input().split())
traps = set(map(int, input().split()))

visited = [False] * N
path = []

def dfs(u):
    visited[u] = True
    path.append(u)

    if u == end:
        return True

    for v in graph[u]:
        if v in traps:
            continue
        if not visited[v]:
            if dfs(v):
                return True

    path.pop()
    return False
if start in traps or end in traps:
    print("Dungeons y Vagos quedan atrapados")
else:
    if dfs(start):
        print(*path)
    else:
        print("Dungeons y Vagos quedan atrapados")