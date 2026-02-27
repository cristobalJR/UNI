maxWeight, nSouvenirs = map(int, input().split())
items = []
valueIn = 0
for _ in range(nSouvenirs):
    items.append(tuple(map(int, input().split())))
items.sort(key=lambda x: x[0]/x[1], reverse=True)

for item in items:
    if item[1] == maxWeight:
        maxWeight -= item[1]
        valueIn += item[0]
        break
    elif item[1] < maxWeight:
        maxWeight -= item[1]
        valueIn += item[0]
    else:
        valueIn += item[0]* (maxWeight/ item[1])
        break

print("{:.2f}".format(valueIn))