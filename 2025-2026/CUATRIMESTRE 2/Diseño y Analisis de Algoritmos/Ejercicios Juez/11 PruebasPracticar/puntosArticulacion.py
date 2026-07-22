# ─────────────────────────────────────────────────────────────────────
# PUNTOS DE ARTICULACIÓN (algoritmo de Tarjan, con UN solo DFS)
# Un punto de articulación es un nodo que, si lo quitas, DESCONECTA el grafo.
# <-- CAMBIA: solo el grafo 'g' (no dirigido). El algoritmo no se toca.
#
# QUÉ GUARDA (esto es lo único que necesitas tener en la cabeza):
#   disc[u]  = INSTANTE en que el DFS pisa u por primera vez (un reloj que solo sube).
#              Se fija una vez y NUNCA cambia.
#   low[u]   = el disc MÁS PEQUEÑO (nodo más "antiguo") al que se puede VOLVER desde u
#              o desde cualquier descendiente suyo, usando como mucho 1 arista de retorno.
#              Es el valor que se va ACTUALIZANDO con min() mientras exploramos.
#   parent[u]= de quién venimos en el árbol DFS (-1 si u es la raíz).
#   time[0]  = reloj global; va en una lista para poder modificarlo por referencia.
#   ap[u]    = True si u es punto de articulación.
#   children = nº de hijos de u en el árbol DFS (solo importa cuando u es la raíz).
#
# CÓMO SE DECIDE (2 casos):
#   • u es la RAÍZ      -> es articulación si tiene 2 o más hijos en el árbol DFS.
#   • u NO es la raíz   -> es articulación si tiene un hijo v cuyo subárbol NO logra
#                          trepar por encima de u, o sea  low[v] >= disc[u]
#                          (entonces u es la única salida de ese subárbol).
# ─────────────────────────────────────────────────────────────────────
def dfs(g, disc, low, parent, time, ap, u):
    disc[u] = low[u] = time[0]            # al entrar en u: disc y low arrancan iguales
    time[0] += 1                          # el reloj avanza para el siguiente nodo
    children = 0
    for v in g[u]:
        if disc[v] == -1:                 # v sin visitar  ->  v es HIJO de u en el árbol DFS
            parent[v] = u
            children += 1
            dfs(g, disc, low, parent, time, ap, v)   # exploro entero el subárbol de v...
            low[u] = min(low[u], low[v])  # ...y heredo lo más alto que alcanzó v
            # CASO 2: u no es raíz y el subárbol de v no sube por encima de u -> u es puente
            if parent[u] != -1 and low[v] >= disc[u]:
                ap[u] = True
        elif v != parent[u]:              # v ya visitado y NO es el padre  ->  ARISTA DE RETORNO
            low[u] = min(low[u], disc[v]) # u puede "trepar" hasta v: se usa disc[v], no low[v]
    # CASO 1: u es la raíz; con 2+ hijos, quitarla dejaría esos subárboles sueltos entre sí
    if parent[u] == -1 and children > 1:
        ap[u] = True

def findArticulationPoints(g):
    v = len(g)
    disc = [-1]*v; low = [-1]*v           # -1 significa "aún no visitado"
    parent = [-1]*v; ap = [False]*v
    time = [1]                            # el reloj empieza en 1
    for i in range(v):                    # recorre todos los nodos por si el grafo
        if disc[i] == -1:                 # tiene varias componentes desconectadas
            dfs(g, disc, low, parent, time, ap, i)
    # el resultado son los nodos marcados como articulación
    return [node for node in range(v) if ap[node]]