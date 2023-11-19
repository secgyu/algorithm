def f(v, s, e, key):
    if s > e:
        return -1
    m = s + (e-s) // 2
    if key < v[m]:
        return f(v, s, m-1, key)
    elif key > v[m]:
        return f(v, m+1, e, key)
    else:
        return m

def f2(v,key):
    s, e = 0, len(v)-1
    while s <= e:
        m = s + (e-s) // 2
        if key < v[m]:
            e = m-1
        elif key > v[m]:
            s = m+1
        else:
            return m
    return -1


v = [1, 10, 20, 30, 40, 50]
print(f(v, 0, len(v)-1, 50))
print(f2(v,50))