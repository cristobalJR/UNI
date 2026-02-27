def entradas():
    n_actividades = int(input())
    actividades = []

    for _ in range(n_actividades):
        actividad, inicio, fin = input().split()
        actividades.append((actividad, int(inicio), int(fin)))

    return actividades

def velada(actividades):
    # Ordenamos las actividades por su tiempo de finalización
    actividades.sort(key=lambda x: x[2])

    n_actividades_realizar = 0
    ultimo_fin = -1

    for actividad in actividades:
        inicio = actividad[1]
        fin = actividad[2]

        if inicio >= ultimo_fin:
            n_actividades_realizar += 1
            ultimo_fin = fin

    return n_actividades_realizar

actividades = entradas()
n_actividades_realizar = velada(actividades)
print(n_actividades_realizar)