import numpy as np

def matrix_multiplication(A, B):
    """

    >>> A = np.array([[1, 0], [0, 1]])
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    array([[4, 1],
           [2, 2]])

    >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
    >>> B = np.array([[4,1], [2,2], [5,1], [2,3]])
    >>> matrix_multiplication(A, B)
    array([[ 9,  2],
           [ 7,  3],
           [21,  8],
           [28,  8]])
    """

    A = np.array(A)
    B = np.array(B)
    return A @ B
