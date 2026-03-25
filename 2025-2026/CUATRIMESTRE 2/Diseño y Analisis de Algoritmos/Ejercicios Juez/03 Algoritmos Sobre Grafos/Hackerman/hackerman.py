'''

La primera línea contiene dos números enteros 𝑁, 𝑀 que representan el número de nodos
que hay en la red de la empresa y el número de conexiones entre nodos.
Las siguientes 𝑁 líneas contendrán un entero 𝑐 que indica el coste de reforzar cada nodo.
Las siguientes 𝑀 líneas contienen dos enteros 𝑎 y 𝑏 que indican los ordenadores
directamente conectados.

6 5
50
22
58
99
38
21
0 1
1 2
2 3
3 4
4 5
'''

n,m = map(int, input().split())
graph = {}
for j in range(n):
    c = int(input())
    graph[j] = {'valor': c , 'vecinos':[]}
for _ in range(m):
    a,b = map(int, input().split())
    graph[a]['vecinos'].append(b)
    graph[b]['vecinos'].append(a)

def articulationPoints(graph):
    lenGraph = len(graph)
    time = [0]
    visited = [False]*lenGraph
    parent = [None]*lenGraph
    disc = [None]*lenGraph
    low = [None]*lenGraph
    articulation = []
    def dfs(u):
        child = 0
        visited[u] = True
        disc[u] = low[u] =time[0]
        time[0] += 1
        for neighbor in graph[u]['vecinos']:
            if not visited[neighbor]:
                child += 1
                parent[neighbor] = u
                dfs(neighbor)
                low[u] = min(low[u], low[neighbor])

                # Caso 1: u no es raíz y low[v] >= disc[u]
                if parent[u] is not None and low[neighbor] >= disc[u]:
                    articulation.append(u)

                # Caso 2: u es raíz con más de un hijo
                if parent[u] is None and child > 1:
                    articulation.append(u)

            elif visited[neighbor] and parent[u]!= neighbor:
                low[u] = min(low[u],disc[neighbor])


    for u in range(lenGraph):
        if not visited[u]:
            dfs(u)

    price = 0
    for i in articulation:
        price += graph[i]['valor']
    return price

print(articulationPoints(graph))