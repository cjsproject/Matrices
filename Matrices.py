from fractions import Fraction
from Bareiss import adjugate

class Matrix:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.mat_arr = []

    def __init__(self, arr):
        temp_mat = []
        temp_row = []
        # number check
        for row in arr:
            for e in row:
                try:
                    temp_row.append(float(e))
                except:
                    raise Exception("Matrix must contain Numbers.")
                    exit()
            temp_mat.append(temp_row)
            temp_row = []
        self.row = len(arr)
        self.col = len(arr[0])
        self.mat_arr = temp_mat


    def __str__(self):
        output = ""
        for row in self.mat_arr:
            output += "[  "
            for element in row:
                if (element % 1.0) > 0:
                    output += str(Fraction(element))
                else:
                    output += str(element)
                output += "  "

            output += "]\n"

        return output

    # adds some row to another row as indexed and updates
    def add(self, row_a, row_b, mult=1):
        temp = []
        i = 0
        for x in self.mat_arr[row_a]:
            a = x + mult * self.mat_arr[row_b][i]
            temp.append(a)
            i += 1

        self.mat_arr[row_a] = temp
        return Matrix(self.mat_arr)

    # multiplies a row by a const and updates
    def mult(self, row, const):
        temp = []
        for e in self.mat_arr[row]:
            a = e * const
            temp.append(a)
        self.mat_arr[row] = temp

        return Matrix(self.mat_arr)

    # swaps rows and updates
    def swap(self, row_a, row_b):
        temp = self.mat_arr[row_a]
        self.mat_arr[row_a] = self.mat_arr[row_b]
        self.mat_arr[row_b] = temp

        return Matrix(self.mat_arr)

    # transposes array/matrix
    def tpose(self):
        arr = self.mat_arr
        temp_mat = [[a for a in col] for col in zip(*arr)]

        self.mat_arr = temp_mat
        return Matrix(self.mat_arr)

    # multiplies matrix by another if defined
    def multMat(self, matrix_b):
        if isinstance(matrix_b, Matrix) and self.col == matrix_b.row:
            mat_a = self.mat_arr
            mat_b = matrix_b.mat_arr
            temp_mat = [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*mat_b)] for A_row in mat_a]
        else:
            raise Exception("must be of type matrix and have defined multiplication dim(axm * mxb) = axb")

        self.mat_arr = temp_mat
        return Matrix(self.mat_arr)

    # returns determinant and adjugate matrix if matrix is square
    def determinant(self):
        if self.row == self.col:
            det, adj = adjugate(self.mat_arr)
            return det, Matrix(adj)
        else:
            raise Exception("Determinants only exist for square matrices")
