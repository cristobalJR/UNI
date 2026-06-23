import copy

n,p,b = map(int,input().split())
data = {'n': n, 'W': p,'minV':b ,'nms': [],'w': [], 'v':[]}

for i in range(n):
    nm,we,wn = map(str,input().split())
    we = int(we)
    wn = int(wn)
    data['nms'].append(nm)
    data['w'].append(we)
    data['v'].append(wn)

def is_feasible(sol, data, i):
    return sol['w']+data['w'][i] <= data['W'] and sol['o'][i] == 0

def add(sol, data, i):
    sol['o'][i] += 1
    sol['v'] += data['v'][i]
    sol['w'] += data['w'][i]
    sol['nms'].append(data['nms'][i])

def remove(sol, data, i):
    sol['o'][i] -= 1
    sol['v'] -= data['v'][i]
    sol['w'] -= data['w'][i]
    sol['nms'].remove(data['nms'][i])

def knapsack_bt(data, sol, best_sol, k):
    if sol['v'] > best_sol['v']:
        best_sol = copy.deepcopy(sol)
    for i in range(k, data['n']):
        if is_feasible(sol, data, i):
            add(sol, data, i)
            best_sol = knapsack_bt(data, sol, best_sol, i)
            remove(sol, data, i)
    return best_sol

sol = {'o': [0]*data['n'], 'v': 0, 'w': 0,'nms': []}
best_sol = {'o': [0]*data['n'], 'v': 0, 'w': 0,'nms': []}
best_sol = knapsack_bt(data, sol, best_sol, 0)

print(*sorted(list(best_sol['nms'])))
print(best_sol['w'], best_sol['v'])
if best_sol['v']<=data['minV']:
    print("VUELVE")
else:
    print("SE VA")