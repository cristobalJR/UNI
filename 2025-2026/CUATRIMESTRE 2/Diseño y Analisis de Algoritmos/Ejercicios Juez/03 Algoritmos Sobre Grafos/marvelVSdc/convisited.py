M, N , P= map(str, input().split())
M = int(M)
N = int(N)
gente = [[] for i in range(M)]
for i in range(M):
    gente[i].append(str(input()))
for _ in range(N):
    n,m = map(int, input().split())
    gente[n].append(m)
    gente[m].append(n)
print(gente)

visited = [False for i in range(M)]
stack = []
sol = [[] for i in range(M)]
for i in range(M):
    visited[i] = True
    stack.append(i)
    while stack:
        u = stack.pop()
        print(u)
        for v in reversed(gente[u][1:]):
            if not visited[v] and gente[u][0] == 'Marvel':
                visited[v] = True
                stack.append(v)
                sol[i].append(v)
            else: print("salto por no marvel")
    print("salto")
print(sol)
# hay un par de cambios con respecto al entregado porque daba error