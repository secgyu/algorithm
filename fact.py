def fact(v):
    n = 1
    for i in range(1, v+1):
        n *= i
    return n


def fact2(v):
    if v == 0:
        return 1
    return v * fact2(v-1)


print(fact(5))
print(fact2(5))
