def money_exchange(value, coins):       # coins ORDENADAS de mayor a menor
    exchange = [0] * len(coins)
    i = 0
    while i < len(coins) and value >= 0:
        exchange[i] = value // coins[i]  # cuántas de esta moneda
        value = value % coins[i]         # resto que queda por devolver
        i += 1
    return exchange

coins = [500,200,100,50,20,10,5,2,1, 0.5,0.2,0.1,0.05,0.02,0.01]
print(money_exchange(4.5, coins))          # → [...,2,...] (2€ con una moneda de 2)