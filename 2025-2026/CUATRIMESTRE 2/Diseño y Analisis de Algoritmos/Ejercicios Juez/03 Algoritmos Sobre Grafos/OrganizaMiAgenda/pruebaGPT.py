invitations, restrictions, contractType, contractBrand = input().split()
invitations = int(invitations)
restrictions = int(restrictions)

event_type = {}
event_brand = {}
ids = []

# Grafo original e indegree original
original_graph = {}
original_indeg = {}

for _ in range(invitations):
    idNum, productType, productBrand = input().split()
    idNum = int(idNum)
    ids.append(idNum)
    event_type[idNum] = productType
    event_brand[idNum] = productBrand
    original_graph[idNum] = []
    original_indeg[idNum] = 0

dependencies = []
for _ in range(restrictions):
    u, v = map(int, input().split())
    dependencies.append((u, v))
    original_graph[u].append(v)
    original_indeg[v] += 1

# 1) Marcar prohibidos
forbidden = set()
for idNum in ids:
    if event_type[idNum] == contractType and event_brand[idNum] != contractBrand:
        forbidden.add(idNum)

# 2) Raíces originales permitidas
roots = []
for idNum in ids:
    if idNum not in forbidden and original_indeg[idNum] == 0:
        roots.append(idNum)

# 3) Alcanzables desde raíces originales sin pasar por prohibidos
reachable = set()
stack = []

for restrictions in roots:
    reachable.add(restrictions)
    stack.append(restrictions)

while stack:
    u = stack.pop()
    for v in original_graph[u]:
        if v in forbidden:
            continue
        if v not in reachable:
            reachable.add(v)
            stack.append(v)

# 4) Subgrafo inducido por los alcanzables
graph = {}
indeg = {}

for idNum in reachable:
    graph[idNum] = []
    indeg[idNum] = 0

for u, v in dependencies:
    if u in reachable and v in reachable:
        graph[u].append(v)
        indeg[v] += 1

# 5) Kahn con desempate por menor id
available = []
for idNum in reachable:
    if indeg[idNum] == 0:
        available.append(idNum)
available.sort()

order = []

while available:
    u = available.pop(0)
    order.append(u)

    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            i = 0
            while i < len(available) and available[i] < v:
                i += 1
            available.insert(i, v)

# 6) Imprimir marcas en orden
answer = []
for idNum in order:
    answer.append(event_brand[idNum])

print(" ".join(answer))