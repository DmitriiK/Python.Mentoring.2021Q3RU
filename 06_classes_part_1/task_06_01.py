from random import randint
from collections.abc import Iterable
import copy


class Matrix:
    def __init__(self, *args):
        self._data = {}
        self.__rows_count = 0
        self.__columns_count = 0
        # seems it does not support overloaded constructors
        # but at least we should distinguesh 2 cases of initializing
        if isinstance(args[0], int) and isinstance(args[1], int):
            self.__rows_count = args[0]
            self.__columns_count = args[1]
            for r_ind in range(self.__rows_count):
                for c_ind in range(self.__columns_count):
                    self._data[(r_ind, c_ind)] = randint(0, 9)

        else:  # intitializing by list of numeric lists
            self.__rows_count = len(args)
            r_ind = 0  # row index
            for r in args:
                if not isinstance(r, Iterable):
                    raise ValueError(f'{r} not an iterable')
                if self.__columns_count > 0 \
                        and self.__columns_count != len(r):
                    raise ValueError('all lists should have the same length')
                self.__columns_count = len(r)
                c_ind = 0  # column index
                for entry in r:
                    self._data[(r_ind, c_ind)] = entry
                    c_ind += 1
                r_ind += 1

    @property
    def Dimension(self) -> tuple:
        """
        Matrix dimension
        :return tuple (number of rows, number of columns):
        :rtype:
        """
        return (self.__rows_count, self.__columns_count)

    def Row(self, ri: int) -> list:
        """
        :param ri: row index
        :type ri: int
        :return: vector, - row of the matrix
        :rtype: list
        """
        return [self.Entry(ri, ci) for ci in range(self.__columns_count)]

    def Column(self, ci: int) -> list:
        """
        :param ci: column index
        :type ci: int
        :return: vector, - column of the matrix
        :rtype:  list
        """
        return [self.Entry(ri, ci) for ri in range(self.__rows_count)]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        if not(self.__columns_count == other.__columns_count
               and self.__rows_count == other.__rows_count):
            return False
        for r_ind in range(self.__rows_count):
            for c_ind in range(self.__columns_count):
                if self._data[(r_ind, c_ind)] == other._data[(r_ind, c_ind)]:
                    continue
                return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented

        if self.__rows_count >= other.__rows_count \
                and self.__columns_count >= other.__columns_count:
            smaller = other
            bigger = self
        else:
            if self.__rows_count < other.__rows_count \
                    and self.__columns_count < other.__columns_count:
                smaller = self
                bigger = other
            else:
                raise ('Dimensions of matrices '
                       'are incompatible for + operations')
        ret = copy.deepcopy(bigger)

        for ri in range(smaller.__rows_count):
            for ci in range(smaller.__columns_count):
                ret._data[(ri, ci)] += smaller._data[(ri, ci)]
        return ret

    def __sub__(self, other):
        return self + (other * -1)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return MultiplyMatrixByScalar(self, other)
        if isinstance(self, Matrix):
            return MatrixMultiplication(self, other)
        else:
            return NotImplemented

    @property
    def IsSquare(self):
        return self.__rows_count == self.__columns_count

    def Entry(self, r_ind: int, c_ind: int):
        return self._data[(r_ind, c_ind)]

    def SetEntry(self, r_ind: int, c_ind: int, value: int):
        self._data[(r_ind, c_ind)] = value

    @property
    def IsSymmetric(self):
        if not self.IsSquare:
            return False
        for r in range(1, self.__rows_count):
            for c in range(0, r):
                if self.Entry(r, c) != self.Entry(c, r):
                    return False
        return True

    def Transpose(self):
        new_d = {}
        rc, cc = self.Dimension
        for ri in range(rc):
            for ci in range(cc):
                new_d[(ci, ri)] = self._data[(ri, ci)]
        self._data = new_d
        self.__rows_count, self.__columns_count = cc, rc

    def Print(self):
        """
        Print 2-d matrix as table
        :return: None
        :rtype:
        """
        for r_ind in range(self.__rows_count):
            r_str = '[{0}]'.format(','.join(
                [str(self.Entry(r_ind, c_ind))
                    for c_ind in range(self.__columns_count)]))
            print(r_str)


def DotProduct(vector1: Iterable, vector2: Iterable):
    ret = sum([i * j for (j, i) in zip(vector1, vector2)])
    return ret
    # same can be done by  vector1 @ vector2


def MatrixMultiplication(m1: Matrix, m2: Matrix) -> Matrix:
    """For matrix multiplication,
    the number of columns in the first matrix
    must be equal to the number of rows in the second matrix.
    The product matrix's dimensions
    are (rows of matrix1) × (columns of matrix2). """
    rc1, cc1 = m1.Dimension
    rc2, cc2 = m2.Dimension
    if cc1 != rc2:
        raise ('Incompatible dimensions')
    rows = []
    for ri in range(rc1):
        row = [DotProduct(m1.Row(ri), m2.Column(ci)) for ci in range(cc2)]
        rows.append(row)
    ret = Matrix(*rows)
    return ret


def MultiplyMatrixByScalar(m: Matrix, num_value) -> Matrix:
    ret = copy.deepcopy(m)
    for keys, val in ret._data.items():
        ret._data[keys] = num_value * val
    return ret
