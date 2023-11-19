def partition(v, low, high):
    i, pivot = low-1, v[high]
    for j in range(low, high):
        if v[j] > pivot:
            continue
        i += 1
        v[i], v[j] = v[j], v[i]
    v[i+1], v[high] = v[high], v[i+1]
    return i+1


def quickSort(v, low, high):
    if low >= high:
        return
    p = partition(v, low, high)
    quickSort(v, low, p-1)
    quickSort(v, p+1, high)


n = int(input())

v = [int(input()) for _ in range(n)]

quickSort(v, 0, len(v)-1)

for num in v:
    print(num)