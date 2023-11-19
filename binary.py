def ft1(v, s, e, key):
    if s > e:
        return -1
    m = s + (e-s) // 2
    if key < v[m]:
        return ft1(v,s,m-1,key)
    elif key > v[m]:
        return ft1(v,m+1,e,key)
    else :
        return m

def ft2(v, key):
    s, e = 0, len(v)-1
    while s <= e:
        m = s+(e-s)//2
        if key < v[m]:
            e = m-1
        elif key > v[m]:
            s = m+1
        else :
            return m
    return -1

v = [10,20,30,40,50,60,70,80,90,100]
print(ft1(v,0,len(v)-1, 100))
print(ft2(v,10))