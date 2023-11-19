def f(n, M):
    if memo[n][M] != -1:
        return memo[n][M]
    if n == 0 or M == 0:
        return 0
    if M < w[n-1]:
        memo[n][M] = f(n-1,M)
    else:
        memo[n][M] = max(f(n-1,M), p[n-1]+f(n-1,M-w[n-1]))
    return memo[n][M]

M = 30
p = [100,300,500]
w = [5,10,25]
memo = []
for i in range(len(w)+1):
    memo.append([-1]*(M+1))
print(f(len(w),M))