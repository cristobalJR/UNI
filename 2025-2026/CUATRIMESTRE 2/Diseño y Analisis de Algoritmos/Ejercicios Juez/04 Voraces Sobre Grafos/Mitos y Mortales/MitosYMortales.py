import math

N, M = map(int, input().split())

edges = []

for i in range(M):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

parent = [i for i in range(N)]
rank = [0] * N


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA == rootB:
        return False

    if rank[rootA] < rank[rootB]:
        parent[rootA] = rootB
    elif rank[rootA] > rank[rootB]:
        parent[rootB] = rootA
    else:
        parent[rootB] = rootA
        rank[rootA] += 1

    return True


edges.sort()

totalCost = 0
mstEdges = []

for d, u, v in edges:
    if union(u, v):
        totalCost += d
        mstEdges.append((u, v, d))

        if len(mstEdges) == N - 1:
            break

fuel = totalCost/5
print(math.ceil(fuel))
