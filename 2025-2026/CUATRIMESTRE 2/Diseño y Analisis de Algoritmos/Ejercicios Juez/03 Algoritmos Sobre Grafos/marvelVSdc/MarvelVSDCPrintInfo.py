M, N , P= map(str, input().split())
M = int(M)
N = int(N)
gente = [[] for i in range(M)]
saga = []
for i in range(M):
    saga.append(str(input()))
for _ in range(N):
    n,m = map(int, input().split())
    if saga[n] == saga[m] and saga[n] == P:
        gente[n].append(m)
        gente[m].append(n)

print(gente)
print(saga)
notVisited = list(range(M))
visited = []
print(notVisited)
sol =[]
def dfs(u):
    notVisited.remove(u)
    visited.append(u)
    for v in gente[u]:
        if v in notVisited:
            print("visitamos", str(v))
            dfs(v)
u=0
while notVisited:
    print("visitaremos", str(u))
    dfs(u)
    if notVisited:
        u = notVisited[0]
    sol.append(list(visited))
    visited = []
salas = 0
print(sol)
for i in sol:
    if len(i) > 1:
        salas += 1
    else:
        if saga[i[0]] == P:
            salas += 1

print(salas)
#seguir por aqui, ya tienes las componentes conexas
#igual no es las componentes conexas porque dice que para ir juntos tienen que ser fansa de la misma saga y además estar relacionados entre ellos, no formar parte del mismo grupo, es decir, solo hay que ignorar los nodos de la saga que no estemos mirando, y comprobar asi las componentes conexas
