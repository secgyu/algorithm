def min(v, s, e):
    if s == e:
        return v[s]
    m = s + (e-s) // 2
    minL = min(v, s, m)
    minR = min(v, m+1, e)

    if minL < minR:
        return minL
    else:
        return minR


v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(v, 0, len(v)-1))
