# ─────────────────────────────────────────────────────────────────────
# KRUSKAL (versión "reetiquetado de componentes")
# Construye el ÁRBOL DE EXPANSIÓN MÍNIMA (MST): conecta TODOS los vértices
# con el MENOR coste total y SIN ciclos.
#
# IDEA EN UNA FRASE: ordena las aristas de menor a mayor peso y ve cogiéndolas;
# coges una solo si une dos trozos del grafo que aún estaban separados.
#
# QUÉ GUARDA (lo único que hay que tener en la cabeza):
#   candidates        = TODAS las aristas como (peso, src, dst), ORDENADAS por peso.
#                       El peso va primero a propósito: así sort() ordena por peso.
#   components[i]     = "etiqueta" del grupo (componente) al que pertenece el vértice i.
#                       Dos vértices están conectados  <=>  tienen la MISMA etiqueta.
#                       Es lo que se va ACTUALIZANDO al fusionar grupos.
#   number_components = cuántos grupos separados quedan. Empieza en V (cada vértice solo)
#                       y baja 1 cada vez que unimos dos. Cuando llega a 1, el MST está listo.
#   sol               = coste total acumulado del árbol (lo que devolvemos).
#
# CÓMO SE DECIDE si una arista (w, src, dst) entra:
#   • Si src y dst tienen DISTINTA etiqueta -> estaban en grupos separados:
#       la arista los une SIN crear ciclo  ->  la cogemos.
#   • Si tienen la MISMA etiqueta -> ya estaban conectados:
#       cogerla cerraría un ciclo  ->  la descartamos.
# ─────────────────────────────────────────────────────────────────────

def sort_candidates(g):
    # Vuelca la lista de adyacencia a una lista plana de aristas (peso, src, dst)
    # y la ordena por peso ascendente. Kruskal SIEMPRE mira las aristas de menor a mayor.
    candidates = []
    for adjs in g:
        for (src, dst, w) in adjs:
            candidates.append((w, src, dst))   # peso PRIMERO -> sort() ordena por peso
    candidates.sort()
    return candidates

def update_components(components, new_id, old_id):
    # FUSIONA dos grupos: todo el que tenga la etiqueta 'old_id' pasa a 'new_id'.
    # Tras esto, los dos trozos comparten etiqueta = quedan conectados.
    for i in range(len(components)):
        if components[i] == old_id:
            components[i] = new_id

def kruskal(g):
    candidates = sort_candidates(g)            # 1) aristas ordenadas por peso
    components = list(range(len(g)))           # 2) al principio CADA vértice es su propio grupo
                                               #    (vértice 0 -> etiqueta 0, vértice 1 -> etiqueta 1, ...)
    number_components = len(components)         #    hay tantos grupos como vértices
    sol = 0
    i = 0
    # Recorremos las aristas (ya de menor a mayor) hasta conectar todo (1 solo grupo)
    while i < len(candidates) and number_components > 1:
        w, src, dst = candidates[i]
        if components[src] != components[dst]:           # ¿están en grupos distintos? (no hay ciclo)
            sol += w                                     # la cogemos: sumamos su peso al MST
            number_components -= 1                       # dos grupos se han fundido en uno
            update_components(components, components[src], components[dst])  # reetiquetamos para fusionar
        i += 1                                           # siguiente arista (más pesada o igual)
    return sol                                  # coste total del árbol de expansión mínima

g = [
    [],                              # 0 (no existe; relleno por ir 1-indexado)
    [(1,3,1), (1,4,2), (1,7,6)],     # vecinos del 1: a 3 (peso1), a 4 (peso2), a 7 (peso6)
    [(2,5,2), (2,6,4), (2,7,7)],     # vecinos del 2
    [(3,4,3), (3,7,5)],              # vecinos del 3
    [(4,5,1), (4,6,9)],              # vecinos del 4
    [(5,7,8)],                       # vecinos del 5
    [],                              # 6
    [],                              # 7
]
print(kruskal(g))   # -> 15