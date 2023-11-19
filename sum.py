def sum(v, s, e):
    if s == e:
        return v[s]
    m = s + (e-s) // 2
    sumL = sum(v,s,m)
    sumR = sum(v,m+1, e)
    return sumL + sumR

v = [1,2,3,4,5]
print(sum(v, 0, len(v)-1))