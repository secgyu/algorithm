def f(money):
    if memo[money] != -1:
        return memo[money]
    if money == 0:
        return 0
    if money < 0:
        return float('inf')
    count = float('inf')
    for i in range(len(coin)):
        count = min(count, 1+f(money-coin[i]))
    memo[money] = count
    return count


money = 25
memo = [-1]*(money+1)
coin = [5, 10]
print(f(money))
