def entradas():
    nCandidatas, tMax = map(int, input().split())
    listaCandidatas = []
    for _ in range(nCandidatas):
        n, t = map(str, input().split())
        listaCandidatas.append([n, int(t)])
    return tMax,listaCandidatas

def ordenEsperaMinimo(tMax,listaCandidatas):
    listaCandidatas.sort(key=lambda x: x[1])
    listaCandidatasTimer = [x.copy() for x in listaCandidatas]
    tEspera = 0
    listaFinal = []
    cita1 = listaCandidatas.pop(0)
    listaCandidatasTimer.pop(0)
    listaFinal.append(cita1)
    tEspera += cita1[1]
    for restante1 in listaCandidatasTimer:
        restante1[1] += cita1[1]

    for _ in listaCandidatasTimer:
        if tEspera <= tMax:
            cita= listaCandidatas.pop(0)
            citaTimer= listaCandidatasTimer.pop(0)
            listaFinal.append(citaTimer)
            tEspera += citaTimer[1]
            for restante in listaCandidatasTimer:
                restante[1] += cita[1]
        else:

            break
    return tEspera, listaFinal ,listaCandidatas

tMax,lista = entradas()
sol = ordenEsperaMinimo(tMax,lista)

print("Seleccionadas:")
for x in sol[1]:
    print(x[0])
print("No Seleccionadas:")
for x in sol[2]:
    print(x[0])
print(sol[0])