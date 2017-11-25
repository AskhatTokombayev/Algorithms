import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)


    def __len__(self):
        return self._n

    def __getitem__(self,k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, k):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = k
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def insert(self, position, value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, position, -1):
            self._A[j] = self._A[j-1]
        self._A[position] = value
        self._n += 1


    def remove(self, value):
        for j in range(self._n):
            if self._A[j] == value:
                for k in range(j,self._n-1,1):
                    self._A[k] = self._A[k+1]
                self._n -= 1
                return
        raise ValueError('Value Not Found')






if __name__ in '__main__':
    new_array = DynamicArray()
    new_array.append(1)
    new_array.append(10)
    new_array.append(50)
    new_array.insert(3,20)
    length = len(new_array)
    #print(length)

    new_array.remove(10)
    new_array.remove(20)


    for i in range(len(new_array)):
        value = new_array[i]
        print(value)

