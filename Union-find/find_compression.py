def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


parent = [1, 3, 3, 4, 4]
print(find(0, parent))
print(find(1, parent))
print(find(2, parent))
print(find(3, parent))
print(find(4, parent))
