from Matrices import Matrix
from copy import deepcopy

if __name__ == '__main__':
    # Construct initial arrayMatrix
    A = [[8, 2],
         [5, 6]]
    print(A)

    # Create Matrix object
    B = Matrix(len(A), len(A), A)
    print(B)

    """Elementary Row Operations"""

    # Add two rows
    B.add(0, 1, mult=-1)
    print(B)

    # Multiply a row by a constant
    B.mult(0, 0.25)
    print(B)

    D = deepcopy(B)

    # Swap rows
    C = B.swap(0, 1)
    print(B, C, D, sep='\n')

