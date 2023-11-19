V = int(input())
E = int(input())
g = []
for i in range(V):
    g.append([])
for i in range(E):
    u, v, w = input().split()
    u, v, w = int(u), int(v), int(w)
    g[u].append((v, w))
print(g)
