enemyNumber = int(input())
v = list(map(int, input().split()))

prefixed = [0]
for x in v:
    prefixed.append(prefixed[-1]+x) #presumamos los niveles y lo guardamos en una lista para no sumarlos luego todas las rondas

rounds = int(input())
levels = []
for i in range(rounds):
    levels.append(int(input()))

def rec_bs(e, low, high, elements):
       if low > high: #caso base
        return -low - 1
       mid= (low + high) // 2
       if elements[mid] == e:
           return mid
       elif e < elements[mid]:
        return rec_bs(e,low, mid +-1,elements)
       elif e > elements[mid]:
           return rec_bs(e, mid+1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements)-1, elements)

for level in levels:
    index = rec_binarySearch(level, v)
    if index < 0:
        index=-index-1
        print(index, prefixed[index])
    else:
        print(index + 1, prefixed[index+1])