def power(num, pow):
    if pow == 0:
        return 1
    else:
        return num*power(num, pow-1)


z=power(2,10)
print(z)