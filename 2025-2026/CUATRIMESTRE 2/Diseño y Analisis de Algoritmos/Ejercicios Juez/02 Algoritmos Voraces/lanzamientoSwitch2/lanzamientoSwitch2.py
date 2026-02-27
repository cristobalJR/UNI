def entradas():
    nColas = int(input())
    colas =[[] for _ in range(nColas)]
    for i in range(nColas):
        nPersonasCola = int(input())
        for j in range(nPersonasCola):
            genteTiempo = tuple(map(str, input().split()))
            colas[i].append((genteTiempo[0], int(genteTiempo[1])))
    return colas

def calcularTiempoMinimo(colas):
    nColas = len(colas)
    for i in range(nColas):
        colas[i].sort(key=lambda x: x[1])
        nPersonasRestantesCola = len(colas[i])
        tEsperaCola = 0
        for persona in colas[i]:
            tEsperaCola += persona[1]*nPersonasRestantesCola
            nPersonasRestantesCola -= 1
        print(" ".join(str(person[0]) for person in colas[i]))
        print(tEsperaCola)

colas = entradas()
calcularTiempoMinimo(colas)