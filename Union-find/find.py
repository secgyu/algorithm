# def find(i, parent):
#     while i != parent[i]:
#         i = parent[i]
#     return i

# def find(i):
#     while i != parent[i]:
#         i = parent[i]
#     return i

def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])
    return parent[i]


parent = [1, 3, 3, 3, 4]
print(find(0))
