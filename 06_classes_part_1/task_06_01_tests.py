from task_06_01 import Matrix
import numpy as np
import pytest


def test_equity():
    a = Matrix(3, 2)
    b = Matrix([1, 2], [4, 5])
    c = Matrix([1, 2], [4, 5])
    assert b == c
    assert a != b
    a.Print()
    print('-----')
    b.Print()


def test_add():
    a = Matrix([5, 1, 7], [2, 4, 0],  [2, 2, 8])
    b = Matrix([0, 8], [1, 2], [7, 4])
    expected_sum = Matrix([5, 9, 7], [3, 6, 0], [9, 6, 8])
    print('test add')
    c = a + b
    a.Print()
    print('+')
    b.Print()
    print('=')
    c.Print()
    assert c == expected_sum


def test_sub():
    a = Matrix([5, 1, 7], [2, 4, 0],  [2, 2, 8])
    b = Matrix([0, 8], [1, 2], [7, 4])
    expected_value = Matrix([5, -7, 7], [1, 2, 0], [-5, -2, 8])
    print('test sub')
    c = a - b
    a.Print()
    print('-')
    b.Print()
    print('=')
    c.Print()
    assert c == expected_value


def test_mult_by_matrix():
    rows_a = [[0, 4, 4], [5, 2, 7]]
    rows_b = [[3, 4], [8, 5], [6, 3]]
    rows_result = [[56, 32], [73, 51]]
    a = Matrix(*rows_a)
    print('multiplication by matrix')
    b = Matrix(*rows_b)
    a.Print()
    print('*')
    b.Print()
    c = a * b
    print('===')
    c.Print()
    print('should be:')
    n_a = np.array(rows_a)
    n_b = np.array(rows_b)
    n_c = n_a.dot(n_b)
    print(n_c)
    expected_result = Matrix(*rows_result)
    assert c == expected_result


def test_mult_by_scalar():
    a = Matrix([5, -7, 7], [1, 2, 0], [-5, -2, 8])
    print('multiplication by scalar')
    result = a * 2
    a.Print()
    print(' * 2 = ')
    result.Print()
    expected_result = Matrix([10, -14, 14], [2, 4, 0], [-10, -4, 16])
    assert result == expected_result


@pytest.mark.parametrize("matrix, is_symmetric", [
    (Matrix([1, 0, 3], [0, 2, 5], [3, 5, 1]), True),
    (Matrix([1, 0, 2], [0, 2, 5], [3, 5, 1]), False)
])
def test_is_symmetric(matrix, is_symmetric):
    matrix.Print()
    assert matrix.IsSymmetric == is_symmetric


@pytest.mark.parametrize("matrix, is_square", [
    (Matrix([1, 2], [4, 5]), True),
    (Matrix([1, 0, 2],  [3, 5, 1]), False)
])
def test_is_square(matrix, is_square):
    matrix.Print()
    assert matrix.IsSquare == is_square


def test_transpose():
    a = Matrix([6, 5, 1], [8, 7, 9])
    expected = Matrix([6, 8], [5, 7], [1, 9])
    print('a=')
    a.Print()
    a.Transpose()
    print('after transpose')
    a.Print()
    assert a == expected
