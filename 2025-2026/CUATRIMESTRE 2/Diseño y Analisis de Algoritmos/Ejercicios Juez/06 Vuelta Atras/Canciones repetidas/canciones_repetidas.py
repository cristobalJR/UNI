N,M,S = map(int,input().split())
graph = [[]for _ in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

justFirst = set(map(int,input().split()))


def is_solution(v, graph):
    return v == len(graph)


def is_feasible(graph, sol, v, color):
    feasible = True
    i = 0
    while feasible and i < len(graph[v]):
        adj = graph[v][i]
        if adj < v:
            feasible = color != sol[adj]
        i += 1
    return feasible



def graph_coloring_bt(graph, k, sol, v):
    if is_solution(v, graph):
        is_sol = True
    else:
        is_sol = False
        tope = 0 if v in justFirst else k - 1
        color = 0
        while not is_sol and color <= tope:
            if is_feasible(graph, sol, v, color):
                sol[v] = color
                sol, is_sol = graph_coloring_bt(graph, k, sol, v+1)
                if not is_sol:
                    sol[v] = -1
            color += 1
    return sol, is_sol


respuesta = "TODOS FUERA"
for k in range(1, S + 1):
    sol = [-1] * len(graph)
    sol, is_sol = graph_coloring_bt(graph, k, sol, 0)
    if is_sol:
        respuesta = k
        break
print(respuesta)