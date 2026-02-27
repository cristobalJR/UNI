def entradas():
    nTiendas = int(input())
    pago = float(input())
    tiendas = []
    for n in range(nTiendas):
        name = input()
        coins = list(map(float, input().split()))
        tienda = {
            'nombre': name,
            'cambios': sorted(coins, reverse=True)
        }
        tiendas.append(tienda)
    return pago,tiendas

def mejorTienda(pago, tiendas):
    cambiosMin = []
    deudas = []

    for tienda in tiendas:
        cambioMin = float("inf")
        dineroRestante = pago
        while True:
            cogida = False
            for cambio in tienda['cambios']:
                if cambio <= dineroRestante:
                    dineroRestante -= cambio
                    cogida = True
                    if cambio < cambioMin:
                        cambioMin = cambio
                    break
            if not cogida:
                break
        deudas.append(dineroRestante)
        cambiosMin.append(cambioMin)

    minCoin = min(cambiosMin)
    indexMejorTienda = 0
    for i, cm in enumerate(cambiosMin):
        if cm == minCoin:
            indexMejorTienda = i

    for i, deuda in enumerate(deudas):
        if deuda == 0:
            continue
        elif deuda <= 1:
            print(f"{tiendas[i]['nombre']} me debe {deuda} euro")
        else:
            print(f"{tiendas[i]['nombre']} me debe {deuda} euros")

    print(f"La mejor tienda es {tiendas[indexMejorTienda]['nombre']} me devuelven monedas de {int(cambiosMin[indexMejorTienda])}")


info = entradas()
mejorTienda(info[0],info[1])