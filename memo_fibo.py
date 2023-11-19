def fibo(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]


def fibo2(n, memo):
    if memo[n] >= 0:
        return memo[n]
    if n < 2:
        memo[n] = n
    else:
        memo[n] = fibo2(n-1, memo) + fibo2(n-2, memo)
    return memo[n]


memo = {}
print(fibo(6, memo))
print(memo)

n = 6
memo = [-1]*(n+1)
print(fibo2(n, memo))
print(memo)
