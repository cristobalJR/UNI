c = int(input().strip())
cList = []

for _ in range(c):
    i, s = map(int, input().strip().split())
    cList.append([i,s])
cList.sort(key=lambda x: x[1], reverse=True)
print(cList[0][0],cList[1][0],cList[0][1]+cList[1][1])

