'''
#1
def is_multiple (n,m):
    if m%n == 0:
        return True
    else:
        return False

result = is_multiple(10,111)
print(result)

'''


'''
#3
def minmax(data):
    n = 0
    min, max = data[0], data[0]
    while n < len(data)-1:
        if max < data[n+1]:
            max = data[n+1]
        if min > data[n+1]:
            min = data[n+1]
        n+=1
    return max, min
z = [1,-8, 9, -2,7,-4,2]
print(minmax(z))
'''


'''
#4
def squares_sum(n):
    summ, k = 0, 0
    while k < n:
        summ+=k*k
        k+=1
    return summ

n = 4
z=squares_sum(n)
print(z)
'''

'''
#print(range(8,-10,-2))
list_comprehension = [2**k for k in range(0,9)]
print(list_comprehension)
'''

''''''
def odd_product(n):
    counter=0
    odd_values = []
    for value in n:
        if value%2 == 1:
            odd_values.append(value)
            counter+=1
            if counter==2:
                print ("There are two odd numbers in the list")
                return odd_values
    print("There are no at lease twoo odd values in the list")


z = [1,3,5,7,9,10]
x=odd_product(z)
print(x)