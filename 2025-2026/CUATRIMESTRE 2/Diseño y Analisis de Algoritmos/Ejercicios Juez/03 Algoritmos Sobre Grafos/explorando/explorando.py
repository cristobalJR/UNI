N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    n,m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

visited = [False] * N
distance = [0 for _ in range(N)]
def dfs(u=0):
    visited[u] = True
    print("-"*distance[u]+str(u))
    for v in graph[u]:
        if not visited[v]:
            distance[v] = distance[u] + 1
            dfs(v)
dfs()