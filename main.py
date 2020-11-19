from Matrices import Matrix
from copy import deepcopy

if __name__ == '__main__':
    # Construct initial array
    arr_a = [[1, 2],
             [5, 6]]
    print(arr_a)

    arr_z = [[1, 2, 8],
             [5, 6, 2]]

    # Create Matrix object
    Z = Matrix(arr_z)
    A = Matrix(arr_a)
    print("A =", A, "Z =", Z, sep='\n')

    """Elementary Row Operations"""

    # Add two rows
    A.add(0, 1, mult=-1)
    print("r1 - r2 = r1", A, sep='\n')

    # Multiply a row by a constant
    A.mult(0, 0.25)
    print("row1*(0.25)" ,A, sep='\n')

    D = deepcopy(A)

    # Swap rows
    C = A.swap(0, 1)
    C.swap(0, 1)
    print("A = ", A, "C = ", C, "D = ", D, sep='\n')

    A.multMat(Z)

    print("A*Z: ", A, sep='\n')

    A.tpose()
    D.tpose()
    print("A = ", A, "D = ", D, sep='\n')
