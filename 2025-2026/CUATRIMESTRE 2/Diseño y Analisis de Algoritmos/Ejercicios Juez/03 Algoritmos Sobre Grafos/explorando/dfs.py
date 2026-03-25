N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# Orden lexicográfico
for u in range(N):
    graph[u].sort()

visited = [False] * N
distance = [0 for _ in range(N)]
stack = [0]


while stack:
    u = stack.pop()
    visited[u] = True
    print("-"*distance[u]+str(u))
    # apilar en inverso para que al hacer pop salga el menor primero
    for v in (graph[u]):
        if not visited[v]:
            visited[v] = True
            distance[v] = distance[u] + 1
            stack.append(v)

