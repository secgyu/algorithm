def search(v, key):
    for i in range(len(v)):
        if v[i] == key:
            return i
    return -1


def search2(v, key, i):
    if i == len(v):
        return -1
    if v[i] == key:
        return i
    return search2(v, key, i+1)


v = [1, 2, 3, 4, 5]
print(search(v, 5))
print(search2(v, 5, 0))
