class Vector:
    def __init__(self,dimension):
        self._coords = [0]*dimension

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i]= self[i] + other[i]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return self._coords != other._coords

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ in '__main__':
    v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
    print(v)
    v[1] = 23            # <0, 23, 0, 0, 0> (based on use of setitem )
    v[-1] = 45           # <0, 23, 0, 0, 45> (also via setitem )
    print(v)          # print 45 (via getitem )
    u = v + v            # <0, 46, 0, 0, 90> (via add )
    print(u)             # print <0, 46, 0, 0, 90>
    total = 0
    for entry in v:  # implicit iteration via len and getitem
        total += entry

    z = len(u)
    print(z)






