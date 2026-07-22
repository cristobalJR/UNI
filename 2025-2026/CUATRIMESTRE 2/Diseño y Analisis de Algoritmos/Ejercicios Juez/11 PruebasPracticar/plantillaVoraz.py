def criterio(c, datos):
    # <-- CAMBIA: valor por el que se elige el "mejor" candidato.
    return datos["duracion"][c]           # aqui: menor duracion (MINIMIZAMOS)

def es_factible(solucion, c, datos):
    # <-- CAMBIA: ¿se puede añadir c sin romper la restriccion?
    usado = sum(datos["duracion"][i] for i in solucion)
    return usado + datos["duracion"][c] <= datos["limite"]

def mejor_candidato(candidatos, datos):
    mejor = None
    mejor_valor = float('inf')                # <-- pon -1 (y ">" abajo) si MAXIMIZAS
    for c in candidatos:
        valor = criterio(c, datos)
        if valor < mejor_valor:            # <-- ">" si MAXIMIZAS
            mejor = c
            mejor_valor = valor
    return mejor

def voraz(datos):
    candidatos = set(range(datos["n"]))    # conjunto de candidatos
    solucion = []
    while candidatos:
        c = mejor_candidato(candidatos, datos)
        candidatos.remove(c)               # nunca se reconsidera
        if es_factible(solucion, c, datos):
            solucion.append(c)
        # if len(solucion) == datos["n"]: break   # <-- (opcional) parada anticipada
    return solucion

datos = {"n": 5, "duracion": [3, 1, 4, 2, 2], "limite": 6}
print(voraz(datos))      # -> [1, 3, 4]