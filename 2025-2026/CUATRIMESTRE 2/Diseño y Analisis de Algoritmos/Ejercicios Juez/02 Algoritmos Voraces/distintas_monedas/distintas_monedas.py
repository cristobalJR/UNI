import math


def entradas():
    caja = int(input())
    tiposMoneda = int(input())
    monedas =[]
    for i in range(tiposMoneda):
        coin = list(map(str,input().split()))
        moneda = {
            'nombre':coin[0],
            'valorEuros': float(coin[1]),
            'cambios': [float(x) for x in coin[2:]]
        }
        monedas.append(moneda)
    compras = int(input())
    pagos = []
    for i in range(compras):
        pay = list(map(str,input().split()))
        pago = {
            'nombreMoneda' : pay[0],
            'valorPago' : float(pay[1])
        }
        pagos.append(pago)

    return caja,monedas,pagos

def calculoCaja(caja,monedas,pagos):
    nPedidos = len(pagos)
    for pago in pagos:
        for moneda in monedas:
            if pago['nombreMoneda'] == moneda['nombre']:
                caja += math.ceil(pago['valorPago']*moneda['valorEuros'])
                cambiosPagados= seleccionarCambios(pago,moneda)
                print(f"Pedido {pagos.index(pago) + 1} paga con "+ " ".join(f"{x:g}" for x in cambiosPagados))
    print("Dinero al final del dia: "+ str(caja))
def seleccionarCambios(pago, moneda):
    pagoRestamte = pago['valorPago']
    listaCambios = []
    while pagoRestamte > 0:
        for cambio in moneda['cambios']:
            while pagoRestamte >= cambio:
                listaCambios.append(cambio)
                pagoRestamte -= cambio
    return listaCambios


info = entradas()
calculoCaja(info[0],info[1],info[2])