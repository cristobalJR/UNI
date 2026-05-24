N, A = map(int, input().split())
servers = list(map(int, input().split()))
attacks = []
requestedServers = set()

for _ in range(A):
    idNum, startNum, endNum = map(int, input().split())
    attacks.append([idNum, startNum, endNum])

    requestedServers.add(startNum)
    requestedServers.add(endNum)


#mergeSort:
def mergeSort(s, start, end):
    if end == start:
        return [s[start]]

    mid = (start + end) // 2
    left = mergeSort(s, start, mid)
    right = mergeSort(s, mid + 1, end)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1


    while j < len(right):
        result.append(right[j])
        j += 1

    return result


v = mergeSort(servers,0,len(servers)-1)

#binSearch:
def rec_bs(e, low, high, elements):
    if low > high:  # caso base
        return -low - 1
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return rec_bs(e, low, mid + -1, elements)
    elif e > elements[mid]:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)

orderedRequested = {}

for r in requestedServers:
    index = rec_binarySearch(r, v)
    orderedRequested[r] = index

maxAttack = 0
bestAttacks = []
for ident, ini, fin in attacks:
    a = orderedRequested[fin] - orderedRequested[ini] + 1
    if a > maxAttack:
        bestAttacks = []
        maxAttack = a
        bestAttacks.append(ident)
    elif a == maxAttack:
        bestAttacks.append(ident)
print(*sorted(bestAttacks))
print(maxAttack)