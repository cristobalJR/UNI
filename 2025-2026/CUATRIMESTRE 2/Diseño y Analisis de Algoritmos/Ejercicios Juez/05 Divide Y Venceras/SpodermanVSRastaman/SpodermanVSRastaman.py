spoderman_for_check = list(map(int, input().split()))
rastaman_for_check = list(map(int, input().split()))
spoderman_limit, rastaman_limit = list(map(int, input().split()))

def rec_bs(e, low, high, elements):
    if low > high:  # caso base
        return low # no le restamos 1 porque los checks cuentan desde 1 no 0
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid + 1 #el +1 porque los checks cuentan desde 1
    elif e < elements[mid]:
        return rec_bs(e, low, mid + -1, elements)
    elif e > elements[mid]:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)

for _ in range(2):
    spoder_sol = rec_binarySearch(spoderman_limit, spoderman_for_check)
    rasta_sol = rec_binarySearch(rastaman_limit, rastaman_for_check)
print(spoder_sol, rasta_sol)
if spoder_sol == rasta_sol:
    print("EMPATE")
elif spoder_sol > rasta_sol:
    print("SPODERMAN")
else:
    print("RASTAMAN")