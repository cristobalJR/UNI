N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

def topsort_lex(g):
    grade = [0] * len(g)
    for u in g:
        for v in g[u]:
            grade[v] += 1

    #cola con todos los de grado 0, ordenada
    q = [u for u in range(len(g)) if grade[u] == 0]
    q.sort()
    result = []
    while q:
        u = q.pop(0)
        result.append(u)
        for v in g[u]:
            grade[v] -= 1
            if grade[v] == 0:
                q.append(v)
        q.sort()
    #devolver None si hay ciclo
    return result if len(result) == len(g) else None

res = topsort_lex(graph)
for v in res:
        print(v, end=' ')
