class Vector:
    def __init__(self,dimension):
        if isinstance(dimension, int):
            self._coords = [0]*dimension
        if isinstance(dimension, list):
            self._coords = dimension

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

    def __mul__(self, coefficient):
        if isinstance(coefficient, int) or isinstance(coefficient,float):
            result = Vector(len(self))
            for item in range(len(self)):
                result[item] = self[item] * coefficient
            return result

        elif isinstance(coefficient, Vector):
            result = Vector(len(self))
            for item in range(len(self)):
                result[item] = self[item] * coefficient[item]
            return result
        else:
            raise ValueError('Dimensions must agree')

    def __rmul__(self, other):
        return self * other


    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return self._coords != other._coords

    def __str__(self):
        #  return str(self._coords)[1:-1]
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ in '__main__':
    v = Vector(5)  # construct five-dimensional <0, 0, 0, 0, 0>
    print(len(v))

    v[1] = 23            # <0, 23, 0, 0, 0> (based on use of setitem )
    v[-1] = 45           # <0, 23, 0, 0, 45> (also via setitem )
    print(str(v))



    y = Vector(5)
    y[1] = 23
    y[-1] = 1
    print(y)

    z = v*y
    print(z)

    z = v*5
    print(z)

    z = 5*v
    print(z)

    y=Vector([1,3,4])
    print(y)

    y = vector(5.5)