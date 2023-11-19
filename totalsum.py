def sum(v):
    total = 0
    for i in range(len(v)):
        total += v[i]
    return total


def sum2(v, i):
    if i == len(v):
        return 0
    return v[i] + sum2(v, i+1)


v = [1, 2, 3, 4, 5]
print(sum(v))
print(sum2(v, 0))
