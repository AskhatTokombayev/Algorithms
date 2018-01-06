from ProgressionClass import Progression

class ArithmeticProgression(Progression):
    def __init__(self, increment = 1, start = 0):
        super().__init__(start)
        self._increment = increment
    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    def __init__(self, base = 2, start = 1):
        super().__init__(start)
        self._base = base
    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first
        self._prev, self._current = self._current, self._prev + self._current


if __name__  == '__main__':
    print('Default Progression:')
    Progression().print_progression(1)
    print('Arithmetic progression with increment 5: ')
    ArithmeticProgression(5).print_progression(10)
    print('Arithmetic progression with increment 5 and start 2: ')
    ArithmeticProgression(5, 2).print_progression(10)
    print('Geometric progression with base 3: ')
    GeometricProgression(3).print_progression(10)
