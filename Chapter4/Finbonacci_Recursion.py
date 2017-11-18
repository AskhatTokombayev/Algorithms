# Input type: Integer
# Return type: Integer
def Fibonacci(n):
    if n > 1:
        return Fibonacci(n-1)+Fibonacci(n-2)
    return 1


z = Fibonacci(6)
print(z)
