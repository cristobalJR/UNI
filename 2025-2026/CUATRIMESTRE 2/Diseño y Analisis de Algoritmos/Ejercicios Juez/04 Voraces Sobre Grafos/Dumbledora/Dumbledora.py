# Entrada
N, M = map(int, input().split())
edges = [[] for _ in range(M)]
graph = [[] for _ in range(N)]
for i in range(M):
    u, v, d = map(int, input().split())
    edges[i] = (u, v, d)
    graph[v].append((v, u, d))
    graph[u].append((u, v, d))

def updateComponents(components, old_id, new_id):
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g):
    components = list(range(len(g)))
    nodeW = [0]*len(g)
    count = len(g)
    mst = 0
    list_edges = []
    for neighbor in g:
        for start,end, distance in neighbor:
            if start < end:
                list_edges.append((distance, start, end))
    list_edges.sort()

    while list_edges and count > 1:
        distance, start, end = list_edges.pop(0)
        if components[start] != components[end]:
            nodeW[start] += distance
            nodeW[end] += distance
            mst += distance
            count -= 1
            updateComponents(components, components[start], components[end])
    return mst, nodeW

totalW, nodeMoney = kruskal(graph)
print(f"Coste total: {totalW}")
for i in range(len(nodeMoney)):
    print(f"H{i}: {nodeMoney[i]}")