M, N , P= map(str, input().split())
M = int(M)
N = int(N)
gente = [[] for i in range(M)]
saga = []
for i in range(M):
    saga.append(str(input()))
for _ in range(N):
    n,m = map(int, input().split())
    if saga[n] == P and saga[m] == P:
        gente[n].append(m)
        gente[m].append(n)
    elif saga[n] == P and saga[m] != P:

print(gente)
print(saga)

visited = [False for i in range(M)]

