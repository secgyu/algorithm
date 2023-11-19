def max(v, s, e):
    if s == e:
        return v[s]
    m = s + (e-s) // 2
    maxL = max(v, s, m)
    maxR = max(v, m+1, e)

    if maxL > maxR:
        return maxL
    else:
        return maxR


v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(v, 0, len(v)-1))
