N = int(input())
samples = []
for _ in range(N):
    sample = list(map(int, input().split()))
    samples.append(sample)


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
            counts[0] += (len(left) - i) #solo se suma cuando el izq es mayor que el derecho, y como la lista izquierda está ordenada se le suma la longitud completa y se le resta el indice
    while i < len(left):
        result.append(left[i])
        i += 1


    while j < len(right):
        result.append(right[j])
        j += 1

    return result

totalCount = 0
for s in samples:
    counts = [0]
    mergeSort(s,0,len(s)-1)
    totalCount += counts[0]
    print(counts[0])
print(totalCount)

