N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    n,m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

for u in range(N):
    graph[u].sort()

distance = [0] * N
visited = [False] * N
visited[0] = True
stack = [0]
while len(stack) != 0:
    node = stack.pop()
    print("-"*distance[node] + str(node))
    for neighbor in reversed(graph[node]):
        if not visited[neighbor]:
            distance[neighbor] = distance[node] + 1
            visited[neighbor] = True
            stack.append(neighbor)

#creo que el problema es que en cierto punto utiliza el orden lexicografico, y como el 7 lleva un rato en el stack siendo su primer padre el nodo 0 lo pone a una distancia de 1
#Probar con DFS recursivo