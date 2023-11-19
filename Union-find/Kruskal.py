def find(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i


def union(i, j, parent, rank):
    i, j = find(i, parent), find(j, parent)
    if i == j:
        return
    if rank[i] < rank[j]:
        parent[i] = j
    elif rank[i] > rank[j]:
        parent[j] = i
    else:
        parent[i] = j
        rank[i] += 1


def kruskal(N, E):
    E.sort(key=lambda e: e[2])
    parent, rank = [0]*N, [0]*N
    for i in range(N):
        parent[i] = i
    i, NumEdge, mst, mstSize, cost = 0, len(E), [], 0, 0
    while i < NumEdge and mstSize < N-1:
        u, v, w = E[i]
        if find(u, parent) != find(v, parent):
            mst.append(E[i])
            mstSize += 1
            cost += w
            union(u, v, parent, rank)
        i += 1
    if mstSize < N-1:
        return [], -1
    else:
        return mst, cost

N,E = int(input()), []
for i in range(int(input())):
    u,v,w = input().split()
    E.append((int(u),int(v),float(w)))
print(kruskal(N,E))
