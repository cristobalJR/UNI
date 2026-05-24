N, M = map(int, input().split())
type_list = list(map(int, input().split()))
raw_types= sorted(set(type_list))

graph = [[] for _ in range(N)]
for i in range(M):
    u,v,d = map(int, input().split())
    graph[u].append((v,d))
    graph[v].append((u,d))


ways_to_check = {}

for i in range(len(type_list)):
    typ = type_list[i]
    if typ not in ways_to_check:
        ways_to_check[typ] = []
    ways_to_check[typ].append(i)



def select_min(dist, visited):
    min_dist = float('inf')
    index = -1
    for i in range(len(dist)):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            index = i
    return index

def dijkstra (graph, start):
    dist = [float('inf')]*len(graph)
    visited = [False] * len(graph)
    dist[start] = 0

    for _ in range(len(graph)):
        next_node = select_min(dist, visited)
        if next_node == -1:
            break

        visited[next_node] = True
        for neigh, weight in graph[next_node]:
            if not visited[neigh]:
                new_dist = dist[next_node] + weight
                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
    return dist

sol = []
for tipo in raw_types:
    nodes = ways_to_check[tipo]
    best = float('inf')

    for u in nodes:
        dist = dijkstra(graph, u)

        for v in nodes:
            if u != v:
                best = min(best, dist[v])

    sol.append(best)

print(*sol)
