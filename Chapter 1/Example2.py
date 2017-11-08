import random

def squares(n):
    result = [k*k for k in range(1,n+1) if n%k==0 and k%5 == 0]
    print(result)

squares(100)

result = divmod(10,2)
print (result)
print(result[0])
print(result[1])

z = random.randrange(1,50,1)
print z

