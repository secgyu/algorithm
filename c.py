def gcd(a, b):
    r1, r2 = a, b
    while r2 > 0:
        q = r1 // r2
        r = r1 - (r2 * q)
        r1 = r2
        r2 = r
    return r1
print(gcd(4, 38))