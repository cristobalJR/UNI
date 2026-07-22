# ─────────────────────────────────────────────────────────────────────
# MERGE SORT (ordenar por DIVIDE Y VENCERÁS) — O(n log n) SIEMPRE
# Parte el vector por la mitad, ordena cada mitad por separado y luego
# MEZCLA las dos mitades ya ordenadas. Es ESTABLE: los elementos iguales
# conservan su orden original.
# <-- CAMBIA: nada del algoritmo; pásale tu vector 'v'.
#
# CLAVE DEL TRUCO: mezclar dos listas YA ordenadas es fácil —vas comparando
# solo sus dos cabezas y eliges la menor. Y ordenar un trozo de 1 elemento
# es gratis (ya está ordenado). Eso es todo el algoritmo.
#
# QUÉ GUARDA cada parte:
#   merge:  left, right = las dos mitades (ya ordenadas) que hay que fundir.
#           l = por qué elemento de 'left' voy.   r = por qué elemento de 'right' voy.
#           i = en qué posición de 'v' escribo ahora (v se rellena en orden).
#   merge_sort: mid   = punto de corte.
#               left/right = COPIAS de las dos mitades (¡importante que sean copias!).
# ─────────────────────────────────────────────────────────────────────

def merge(left, right, v):                # funde dos listas ordenadas DENTRO de v
    l = r = i = 0
    while l < len(left) and r < len(right):   # mientras queden elementos en AMBAS
        if left[l] <= right[r]:           # comparo las dos cabezas; '<=' -> ESTABLE
            v[i] = left[l]; l += 1        #   (ante empate, primero el de la izquierda)
        else:
            v[i] = right[r]; r += 1
        i += 1                            # avanzo la posición de escritura en v
    # una de las dos mitades se vació; la OTRA ya está ordenada -> copio su resto tal cual
    resto, f = (left, l) if r == len(right) else (right, r)
    for j in range(f, len(resto)):
        v[i] = resto[j]; i += 1

def merge_sort(v):                        # ordena v EN EL SITIO
    if len(v) == 1:
        return                            # caso base: 1 elemento ya está ordenado
    mid = len(v) // 2
    left  = v[:mid]                       # COPIA de la mitad izquierda
    right = v[mid:]                       # COPIA de la mitad derecha
    merge_sort(left)                      # ordeno cada copia por separado...
    merge_sort(right)
    merge(left, right, v)                 # ...y las fundo de vuelta SOBRE v


v = [5, 2, 9, 1, 5, 6, 3]
merge_sort(v)
print(v)