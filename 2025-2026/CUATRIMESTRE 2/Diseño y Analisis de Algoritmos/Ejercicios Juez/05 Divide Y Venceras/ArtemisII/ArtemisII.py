N = int(input())
samples = list(map(int, input().split()))

def MaxArray(list): #se puede hacer más eficiente con indices i j(inicio fin) para no tener que crear muchas listas distintas, y solo recorrer secciones marcadas por los indices
    if len(list) == 1:
        return list[0]
    mid = len(list)//2
    izq = list[0:mid]
    der = list[mid:]
    max_izq = MaxArray(izq)
    max_der = MaxArray(der)
    max_mid = CalcMaxMid(list, mid)

    return max(max_izq, max_der, max_mid)

def CalcMaxMid(list, mid):
    sum = 0
    max_izq = - float('inf')
    for num in list[mid-1::-1]:
        sum += num
        if sum > max_izq:
            max_izq = sum

    sum = 0
    max_der = - float('inf')
    for num in list[mid:]:
        sum += num
        if sum > max_der:
            max_der = sum
    return max_izq + max_der

print(MaxArray(samples))