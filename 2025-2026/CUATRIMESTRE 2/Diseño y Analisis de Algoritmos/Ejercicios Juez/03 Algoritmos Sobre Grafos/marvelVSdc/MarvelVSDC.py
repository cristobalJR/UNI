M, N , P= map(str, input().split())
M = int(M)
N = int(N)
gente = [[] for i in range(M)]
saga = []
for i in range(M):
    saga.append(input().strip())
for _ in range(N):
    n,m = map(int, input().split())
    if saga[n] == saga[m] and saga[n] == P:
        gente[n].append(m)
        gente[m].append(n)

notVisited = list(range(M))
visited = []
sol =[]
def dfs(u):
    notVisited.remove(u)
    visited.append(u)
    for v in gente[u]:
        if v in notVisited:
            dfs(v)
while notVisited:
    u = notVisited[0]
    visited = []
    dfs(u)
    sol.append(visited[:])
salas = 0
for i in sol:
    if len(i) > 1:
        salas += 1
    else:
        if saga[i[0]] == P:
            salas += 1

print(salas)
