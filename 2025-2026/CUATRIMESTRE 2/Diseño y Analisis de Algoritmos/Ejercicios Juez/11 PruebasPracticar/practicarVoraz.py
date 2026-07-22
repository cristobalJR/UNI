profit=[50,10,15,30]; deadline=[2,1,2,1]

def getBest(candidates,profit):
    bestCandidate,bestProfit =None, -1
    for candidate in candidates:
        if profit[candidate] > bestProfit:
            bestCandidate = candidate
            bestProfit = profit[candidate]
    return bestCandidate


def schedule(profit, deadline):
    candidates = set(range(len(profit)))
    maxDate = max(deadline)
    sol = [-1]* (maxDate + 1)

    while candidates:
        best = getBest(candidates,profit)
        candidates.remove(best)
        i = deadline[best]
        found = False
        while i > 0 and not found:
            if sol[i] == -1:
                sol[i] = best
                found = True
            i-=1

    return sol[1:]

print(schedule(profit, deadline))

