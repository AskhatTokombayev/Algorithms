def product(m,n):

    return 0 if n == 0 else m+product(m, n-1)

#    if n == 0:
#        return 0
#    n-=1
#    return m + product(m, n)

Z = product(81,90)
print(Z)