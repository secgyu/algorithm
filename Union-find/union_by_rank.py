def find(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i


def union(i, j, parent, rank):
    i = find(i, parent)
    j = find(j, parent)
    if i == j:
        return
    if rank[i] < rank[j]:
        parent[i] = j
    elif rank[i] > rank[j]:
        parent[j] = i
    else:
        parent[i] = j
        rank[j] += 1


parent = [1, 1, 3, 3, 5, 5]
rank = [0, 1, 0, 1, 0, 1]

union(0, 2, parent, rank)
union(1, 3, parent, rank)

print(parent)
print(rank)
