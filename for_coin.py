def f(coin, money):
    dp = [0]*(money+1)
    for m in range(1, money+1):
        dp[m] = float('inf')
        for i in range(len(coin)):
            if m >= coin[i]:
                dp[m] = min(dp[m], 1+dp[m-coin[i]])
    return dp[money]


coin = [5, 10]
print(f(coin, 25))
