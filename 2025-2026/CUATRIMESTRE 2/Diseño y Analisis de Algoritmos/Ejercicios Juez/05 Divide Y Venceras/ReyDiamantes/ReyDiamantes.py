N = int(input())
number_list = []
for _ in range(N):
    row = list(map(int, input().split()))
    for num in row:
        number_list.append(num)

atack_list = list(map(int, input().split()))


#binSearch:
def rec_bs(e, low, high, elements):
    if low > high:  # caso base
        return low
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return rec_bs(e, low, mid + -1, elements)
    elif e > elements[mid]:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)


sol = []
used = [False] * len(number_list)

for a in atack_list:
    s = rec_binarySearch(a, number_list)

    while s < len(number_list) and used[s]:
        s += 1

    if s < len(number_list):
        sol.append(s)
        used[s] = True

for i in sol:
   number_list[i] = "X"

for i in range(0, len(number_list), N):
    print(*number_list[i:i+N])