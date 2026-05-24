N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(M):
    u, v, d, p = map(int, input().split())
    graph[u].append((v, d, p))
    graph[v].append((u, d, p))
NGoals = int(input())
goals = []

for _ in range(NGoals):
    g = int(input())
    goals.append(g)


def select_min(dist, visited):
    min_dist = float('inf')
    index = -1

    for i in range(len(dist)):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            index = i

    return index


def dijkstra(graph, start):
    dist = [float('inf')] * len(graph)
    visited = [False] * len(graph)
    parent = [-1] * len(graph)

    dist[start] = 0

    for _ in range(len(graph)):
        next_node = select_min(dist, visited)

        if next_node == -1:
            break

        visited[next_node] = True

        for neigh, weight, restriction in graph[next_node]:
            if not visited[neigh] and (restriction == -1 or visited[restriction]):
                new_dist = dist[next_node] + weight

                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    parent[neigh] = next_node

    return dist, parent


dist, parent = dijkstra(graph, 0)


for goal in goals:
    if dist[goal] == float('inf'):
        print("MISION FALLIDA")
    else:
        trail = []
        i = goal

        while i != -1:
            trail.append(i)
            i = parent[i]

        trail.reverse()

        print(*trail, "-", dist[goal])