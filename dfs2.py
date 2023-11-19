def dfs(u):
    visited[u] = 1
    print(u, '=>', end=' ')
    for v in g[u]:
        if visited[v] == 0:
            dfs(v)


g = [[1], [0, 3, 4], [5, 6], [1], [1], [2, 7], [2, 7], [5, 6]]
N = len(g)
visited = [0]*N
dfs(1)
