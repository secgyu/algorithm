def dfs(g, u, visited):
    visited[u] = 1
    print(u, '=>', end=' ')
    for v in g[u]:
        if visited[v] == 0:
            dfs(g, v, visited)


G = [[1, 2], [0, 3, 4], [0, 5, 6], [1, 7],
     [1, 7], [2, 7], [2, 7], [3, 4, 5, 6]]
N = 8
visited = [0]*N
print(dfs(G, 0, visited))
