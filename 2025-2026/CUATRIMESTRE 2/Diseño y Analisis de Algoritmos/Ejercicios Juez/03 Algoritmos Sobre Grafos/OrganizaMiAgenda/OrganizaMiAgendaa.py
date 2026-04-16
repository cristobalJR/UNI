invitations,restrictions,contractType,contractBrand = input().split()
invitations = int(invitations)
restrictions = int(restrictions)
event_type = {}
event_brand = {}
ids =[]

# Grafo original
original_graph = {}
original_indegree = {}

for _ in range(invitations):
    idNum, productType, productBrand = input().split()
    idNum = int(idNum)
    ids.append(idNum)
    event_type[idNum] = productType
    event_brand[idNum] = productBrand
    original_graph[idNum] = []
    original_indegree[idNum] = 0

dependencies =[]
for _ in range(restrictions):
    u,v = map(int,input().split())
    dependencies.append((u,v))
    original_graph[u].append(v)
    original_indegree[v] += 1

# 1)Marcar prohibidos
forbidden = set()
for idNum in ids:
    if event_type[idNum] == contractType and event_brand[idNum] != contractBrand:
        forbidden.add(idNum)

# 2)Calcular raices originales permitidas
roots = []
for idNum in ids:
    if idNum not in forbidden and original_indegree[idNum] == 0:
        roots.append(idNum)

# 3)Alcanzables desde raices originales sin pasar por prohibidos
reachable = set()
stack = []
for r in roots:
    reachable.add(r)
    stack.append(r)

while stack:
    node = stack.pop()
    for neighbor in original_graph[node]:
        if neighbor in forbidden:
            continue
        if neighbor not in reachable:
            reachable.add(neighbor)
            stack.append(neighbor)

# subgrafo formado por los alcanzables
graph = {}
in_degree = {}

for idNum in reachable:
    in_degree[idNum] = 0
    graph[idNum] = []

for u, v in dependencies:
    if u in reachable and v in reachable:
        graph[u].append(v)
        in_degree[v] += 1

# 4)Kahn eligiendo por ID más bajo

queue = [node for node in reachable if in_degree[node] == 0] #cola nodos grado entrada 0
queue.sort()

topo_ordered = [] #lista resultado

#procesar hasta su vaciado
while queue:
    current = queue.pop(0)
    topo_ordered.append(current)

    for neighbor in graph[current]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            i = 0
            while i < len(queue) and queue[i] < neighbor:
                i += 1
            queue.insert(i, neighbor)
# de esta forma insertamos neighbor en su sitio de la lista sin tener que ordenarla todo el rato y desordenarla cuando metas otro para volver a ordenar
# 5)Imprimir en orden
sol = []
for topo in topo_ordered:
    sol.append(event_brand[topo])

print(" ".join(sol))