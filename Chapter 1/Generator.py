def factors(x):
    k = 1
    while k*k<x:
        if x%k == 0:
            yield k
            yield x//k
        if k*k == n:
            yield k
        k += 1




y = factors(100)
for n in y:
    print(n)