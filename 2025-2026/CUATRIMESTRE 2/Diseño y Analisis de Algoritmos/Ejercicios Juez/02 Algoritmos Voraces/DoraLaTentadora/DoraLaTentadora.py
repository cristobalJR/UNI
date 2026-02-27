def greedy_schedule(profit, deadline):
    n = len(profit)
    candidates = list(range(n))
    candidates.sort(key=lambda i: profit[i], reverse=True)
    last_date = max(deadline)
    sol = [-1] * (last_date + 1)
    filled = 0
    for best in candidates:
        if filled == last_date + 1:
            break
        i = deadline[best]
        while i >= 0:
            if sol[i] == -1:
                sol[i] = best
                filled += 1
                break
            i -= 1

    return sol, last_date

nTentadores = int(input())
names = []
profit = []
deadline = []
for i in range(nTentadores):
    line = list(map(str, input().split()))
    names.append(line[0])
    deadline.append(int(line[1]))
    profit.append(int(line[2]))

sol, lastDate = greedy_schedule(profit, deadline)
for i in range(lastDate + 1):
    if sol[i] != -1:
        print(f"DIA {i}: {names[sol[i]]}, LE SOBRAN {deadline[sol[i]] - i} DIAS")
    else:
        print(f"DIA {i}: SIN TENTADOR")