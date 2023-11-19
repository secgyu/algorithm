def partition(v,low,high):
    i, pivot = low-1, v[high]
    for j in range(low, high):
        if v[j] > pivot:
            continue
        i+=1
        v[i],v[j] = v[j],v[i]
    v[i+1],v[high] = v[high],v[i+1]
    return i+1

def quickSort(v,low,high):
    if low >= high:
        return
    p = partition(v,low,high)
    quickSort(v,low,p-1)
    quickSort(v,p+1,high)

v = [100, 50, 90, 80, 60, 70, 40, 30, 20, 10]
quickSort(v,0,len(v)-1)
print(v)