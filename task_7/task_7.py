class MyMatrix:
    def __init__(self, matrix):
        self._matrix = matrix

    def __str__(self):
        print('\n')
        for i in self._matrix:
            print(' '.join(map(str, i)))

    def __add__(self, other):
        for i, x in enumerate(self._matrix):
            for j, y in enumerate(x):
                self._matrix[i][j] = self._matrix[i][j] + other[i][j]


from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.nameClothes = name

    @abstractmethod
    def fabricConsumption(self, P):
        pass


class Coat(Clothes):
    # def __init__(self, name):
    #    super().__init__(name)

    def fabricConsumption(self, V):
        return V / 6.5 + 0.5


class Suit(Clothes):

    # def __init__(self, name):
    #    super().__init__( name)

    def fabricConsumption(self, H):
        return 2 * H + 0.3


class Cells:
    def __init__(self, count):
        self._count = count

    def __add__(self, other):
        return Cells(self._count + other._count)

    def __sub__(self, other):

        s = self._count - other._count
        if s > 0:
            return Cells(s)
        else:
            print('warning sub <= 0')
            return Cells(0)

    def __mul__(self, other):
        return Cells(self._count * other._count)

    def __truediv__(self, other):
        return Cells(self._count % other._count)

    def make_order(self, count_in_row):
        print(f'\nmake_order _count = {self._count}, step =  {count_in_row}')
        s = '*' * self._count
        list = [s[i:i + count_in_row] for i in range(0, self._count, count_in_row)]
        s = '\n'.join(list)
        print(s)


class MyTask:

    @property
    def task_1(self):
        print(f'ask 1')
        m = MyMatrix([[1, 2, 3, 33], [4, 5, 6, 66], [7, 8, 9, 99]])
        m.__str__()
        m.__add__([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]])
        m.__str__()

    @property
    def task_2(self):
        print(f'Task 2')

        V = 180
        coat = Coat('coat')
        print(f'\n {coat.nameClothes} of fabric consumption per V{V} = {coat.fabricConsumption(V)}')
        H = 90
        suit = Suit('suit')
        print(f'\n {suit.nameClothes} of fabric consumption per V{H} = {suit.fabricConsumption(H)}')

    @property
    def task_3(self):
        print(f'Task 3')
        c1 = Cells(100)
        c2 = Cells(10)
        c3 = [c1 + c2, c1 - c2, c2 - c1, c1 / c2, c2 / c1, c1 * c2]
        print([i._count for i in c3])

        c2.make_order(4)


if __name__ == '__main__':
    mt = MyTask()
    mt.task_1
    mt.task_2
    mt.task_3
