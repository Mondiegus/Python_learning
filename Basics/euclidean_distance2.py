from math import sqrt

def euclidean_distance(A, B):
    """
    >>> A = (0,1,0,1)
    >>> B = (1,1,0,0)
    >>> euclidean_distance(A, B)
    1.4142135623730951

    >>> euclidean_distance((0,0,0), (0,0,0))
    0.0

    >>> euclidean_distance((0,0,0), (1,1,1))
    1.7320508075688772

    >>> euclidean_distance((0,1,0,1), (1,1,0,0))
    1.4142135623730951

    >>> euclidean_distance((0,0,1,0,1), (1,1,0,0,1))
    1.7320508075688772

    >>> euclidean_distance((0,0,1,0,1), (1,1))
    Traceback (most recent call last):
        ...
    ValueError: Points must be in the same dimensions
    """

    count = 0
    if len(A) != len(B):
        raise ValueError('Points must be in the same dimensions')
    else:
        for n1, n2 in zip(A, B):
            count += (n2-n1)**2

    return sqrt(count)