# ─────────────────────────────────────────────────────────────────────
# DIJKSTRA (camino más corto desde UN origen a todos los demás; pesos >= 0)
# Algoritmo VORAZ: en cada paso "cierra" el nodo no visitado MÁS CERCANO al
# origen, y una vez cerrado su distancia ya es DEFINITIVA.
# <-- CAMBIA: solo la lectura del grafo 'g' (g[u]=lista de (src,dst,peso), 0-indexado) y 'start'.
#
# QUÉ GUARDA (lo único que hay que tener en la cabeza):
#   distances[v] = mejor distancia conocida del origen a v HASTA AHORA.
#                  Se va mejorando con min(); cuando v se "cierra", es definitiva.
#   visited[v]   = True si v ya está CERRADO (su distancia ya no va a cambiar).
#   0x3f3f3f3f   = "infinito" = aún no alcanzado. Es ~10^9: lo bastante grande
#                  para que 'infinito + peso' no desborde ni parezca un camino real.
#   next_node    = el nodo no cerrado más cercano al origen (el que cerramos ahora).
#
# POR QUÉ FUNCIONA (la idea voraz):
#   Si eliges el nodo no visitado con MENOR distancia, esa distancia ya no puede
#   mejorar: cualquier otro camino hacia él pasaría antes por un nodo MÁS LEJANO,
#   así que no habría atajo. Por eso es seguro darlo por cerrado.
#
# CÓMO SE ACTUALIZA (relajación):
#   distances[dst] = min(distances[dst], distances[src] + w)
#   = "¿llego a dst más barato pasando por el nodo que acabo de cerrar (src)?"
# ─────────────────────────────────────────────────────────────────────

def select_min(distances, visited):
    # Devuelve el nodo NO cerrado con menor distancia (el próximo a cerrar).
    next_node = 0
    min_dist = float('inf')
    for i in range(len(distances)):       # 0-indexado: recorre TODOS los nodos (0..n-1)
        if not visited[i] and distances[i] < min_dist:
            next_node = i
            min_dist = distances[i]
    return next_node

def dijkstra(g, start):
    n = len(g)                            # nº de vértices (nodos 0..n-1, sin relleno)
    distances = [float('inf')] * n          # todos a "infinito"...
    visited = [False] * n
    distances[start] = 0                  # ...menos el origen, que está a 0 de sí mismo
    visited[start] = True                 # cerramos el origen
    for src, dst, w in g[start]:          # arranque: distancia directa a los vecinos del origen
        distances[dst] = w                #   (en grafo simple hay 1 sola arista por vecino)
    for _ in range(n - 1):                # quedan n-1 nodos por cerrar
        next_node = select_min(distances, visited)   # 1) el más cercano aún no cerrado
        visited[next_node] = True         # 2) lo cerramos: su distancia ya es definitiva
        for src, dst, w in g[next_node]:  # 3) RELAJACIÓN: intento abaratar a sus vecinos
            distances[dst] = min(distances[dst], distances[src] + w)
    return distances                      # distances[v] = distancia mínima origen -> v
g = [
    [(0,1,4), (0,2,1)],   # vecinos del 0
    [(1,3,1)],            # vecinos del 1
    [(2,1,2), (2,3,5)],   # vecinos del 2
    [(3,4,3)],            # vecinos del 3
    [],                   # 4
]
print(dijkstra(g, 0))   # -> [0, 3, 1, 4, 7]