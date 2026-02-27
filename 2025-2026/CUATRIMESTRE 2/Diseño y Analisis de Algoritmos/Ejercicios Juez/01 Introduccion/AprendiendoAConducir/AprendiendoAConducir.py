n = int(input())


iSet = {
    'Arranca':'Mete primera y pisa acelerador',
    'Cambia de marcha':'Pisa embrague a fondo',
    'Para': 'Pisa freno y embrague',
    'Aparca':'Imposible',
    'Rotonda':'POR EL CARRIL DERECHO',
    'Gira':'El intermitente, por favor'
}

for _ in range(n):
    situacion = input().strip()
    print(iSet.get(situacion))


