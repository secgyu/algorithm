def f(money):
    if memo[money] != -1:
        return memo[money]
    if money == 0:
        return 0
    if money < 0:
        return float('inf')
    count = float('inf')
    coinUsed = -1
    for i in range(len(coin)):
        new_count = 1+f(money - coin[i])
        if new_count < count:
            count = new_count
            coinUsed = coin[i]
    memo[money] = count
    P[money] = coinUsed
    return count


def printCoinChange(money):
    if P[money] == -1:
        print('교환불가')
        return
    while money > 0:
        print(P[money])
        money -= P[money]


coin, money = [5, 10], 25
memo, P = [-1]*(money+1), [-1]*(money+1)
print(f(money))
printCoinChange(money)
