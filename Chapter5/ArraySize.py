import sys
Array = [0]
for k in range(10):
    length = len(Array)
    size = sys.getsizeof(Array)

    print('Length: {0:3d}, Size in bytes {0:4d}'.format(length,size))
    Array.append(None)
    print(Array)