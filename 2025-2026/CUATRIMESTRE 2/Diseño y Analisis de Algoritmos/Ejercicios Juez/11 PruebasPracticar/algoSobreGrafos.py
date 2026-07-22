# Grafo dirigido acíclico:
n = 6
g = [
    [2, 3],    # nodo 0
    [3, 4],    # nodo 1
    [5],       # nodo 2
    [5],       # nodo 3
    [5],       # nodo 4
    []         # nodo 5
]
# <-- CAMBIA: la lectura del grafo dirigido 'g' y 'n'. Imprime -1 si hay ciclo.
def lexic_top_sort(g, n):
    aristas_entrantes = [0] * n
    for u in range(n):
        for v in g[u]:
            aristas_entrantes[v] += 1     # contar grado de entrada

    nodos_iniciales = [i for i in range(n) if aristas_entrantes[i] == 0]
    topological_sort = []
    cnt = 0
    while nodos_iniciales:
        nodos_iniciales.sort()            # ← orden lexicográfico (determinismo)
        origen = nodos_iniciales.pop(0)
        topological_sort.append(origen)
        for adj in g[origen]:             # "eliminar" aristas salientes
            aristas_entrantes[adj] -= 1
            if aristas_entrantes[adj] == 0:
                nodos_iniciales.append(adj)
        cnt += 1
    if cnt != n:                          # no salieron todos -> CICLO
        print(-1); return
    for tarea in topological_sort:
        print(tarea, end=' ')

lexic_top_sort(g, n)