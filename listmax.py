def maxList(v):
    max = v[0]
    for i in range(len(v)):
        if max < v[i]:
            max = v[i]
    return max

def maxList2(v,i):
    if i == len(v)-1:
        return v[i]
    return max(v[i], maxList2(v,i+1))

v = [10,5,9,2,7,0]
print(maxList(v))
print(maxList2(v,0))