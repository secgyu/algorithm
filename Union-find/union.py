def find(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i


def union(i, j, parent):
    i = find(i, parent)
    j = find(j, parent)
    if i == j:
        return
    parent[i] = j


parent = [1, 2, 2, 4, 4]

union(0, 1, parent)
union(1, 2, parent)
union(2, 3, parent)
union(3, 4, parent)

print(parent)
