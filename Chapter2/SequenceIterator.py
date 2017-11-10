class SequenceIterator:
    def __init__(self,sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise   StopIteration()

    def __len__(self):
        return len(self._seq)

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self._seq[item]

    def __setitem__(self, key, value):
        self._seq[key] = value


    def __add__(self,added):
        if len(self) == len(added):
            result = SequenceIterator([0]*((len(self))))
            for i in range(len(self)):
                result[i] = self._seq[i] + added[i]
            return result



if __name__ in '__main__':
    z = SequenceIterator([4,3,2,1])
    q = SequenceIterator([9,8,7,6])
    a=z+q

    for i in range(len(a)):
        q=next(a)
        print(q)