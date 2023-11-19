V = int(input())
E = int(input())
g = []
for i in range(V):
    g.append([0]*V)
for i in range(E):
    u,v = input().split()
    u,v = int(u), int(v)
    g[u][v] = 1
    g[v][u] = 1
print(g)

