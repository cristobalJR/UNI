nSouvenirs =int(input())
items = []
valueIn = 0
for _ in range(nSouvenirs):
    datos = input().split()
    fila = [datos[0]] + list(map(int, datos[1:]))
    items.append(fila) #datos de entrada formateados
space = list(map(int, input().split()))

# en cada habitación se ordenará la lista de una manera

for s in range(len(space)):
    maxWeight = space[s]
    items.sort(key=lambda x: x[s+2] / x[1], reverse=True)
    counting = 0
    for item in items:
        counting+=1
        if item[1] == maxWeight:
            maxWeight -= item[1]
            valueIn += item[s+2]
            item[2:4] = [0,0,0]
            break
        elif item[1] < maxWeight:
            maxWeight -= item[1]
            valueIn += item[s+2]
            item[2:4] = [0,0,0]
        else:
            valueIn += item[s+2]* (maxWeight/ item[1])
            item[2:4] = [0,0,0]
            break
    print(f"HABITACION {s}: {valueIn:.2f}")
    for i in range(counting):
        print(items[i][0])
    valueIn = 0
