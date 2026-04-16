invitations,restrictions,contractType,contractBrand = input().split()
invitations = int(invitations)
restrictions = int(restrictions)
contract = (contractType,contractBrand)
events = dict()
for _ in range(invitations):
    idNum, productType, productBrand = input().split()
    events[int(idNum)] = (productType,productBrand)
forbiden = [False] * invitations
graph = dict()
for _ in range(restrictions):
    u,v = map(int, input().split())

    if u not in graph:
        graph[u] = set()
    if v not in graph:
        graph[v] = set()
    if events[u][0] == contract[0] and events[u][1] != contract[1]:
        forbiden[u] = True
    if events[v][0] == contract[0] and events[v][1] != contract[1]:
        forbiden[v] = True
        continue
    else:
        graph[u].add(v)

def kahn(graph):
    #conteo grado entrada
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = [node for node in in_degree if in_degree[node] == 0] #cola nodos grado entrada 0
    queue.sort()
    topo_ordered = [] #lista resultado

    #procesar hasta su vaciado
    while queue:
        current = queue.pop(0)
        topo_ordered.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                queue.sort()
    return topo_ordered

print(forbiden)
print(contract)
print(events)
print(graph)
print(kahn(graph))