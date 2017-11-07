def fibonacci(n):
    a = 0;
    b = 1;
    while a <= n:
        yield a
        c = a+b
        a = b
        b = c





for n in fibonacci (1000):
    print(n)