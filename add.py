def add(v):
    for i in range(len(v)):
        v[i] += 1


def add2(v, i):
    if i == len(v):
        return
    v[i] += 1
    add2(v, i+1)


v = [1, 2, 3, 4, 5]
add(v)
print(v)

add2(v, 0)
print(v)
