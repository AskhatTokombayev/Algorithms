class Range:
    def __init__(self, start, stop = None, step = 1):

        if step == 0:
            raise ValueError('step cannot be 0')
        if stop == None:
            start, stop = 0, start
        self._length = max(0, (stop - start +step - 1)//step)
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, item):
        if item < 0:
            item += len(self)

        if not 0 <= item < self._length:
            raise IndexError('index out of range')

        return self._start + item*self._step


if __name__ in '__main__':
    x = Range(0,5,1)
    length = len(x)
    print(length)
    z = x[0]
    print(z)

    for k in Range(20,40,7):
        print(k)




