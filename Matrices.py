from fractions import Fraction

class Matrix:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.mat_arr = []

    def __init__(self, n, m, arr):
        temp_mat = []
        temp_row = []
        #number check
        for row in arr:
            for e in row:
                try:
                    temp_row.append(float(e))
                except:
                    print("Matrix must contain Numbers.")
                    exit()
            temp_mat.append(temp_row)
            temp_row = []
        self.row = n
        self.col = m
        self.mat_arr = temp_mat

    def add(self, row_a, row_b, mult=1):
        temp = []
        i = 0
        for x in self.mat_arr[row_a]:
            a = x + mult*self.mat_arr[row_b][i]
            temp.append(a)
            i += 1
        self.mat_arr[row_a] = temp

        return Matrix(self.row, self.col, self.mat_arr)


    def mult(self, row, const):
        temp = []
        for e in self.mat_arr[row]:
            a = e * const
            temp.append(a)
        self.mat_arr[row] = temp

        return Matrix(self.row, self.col, self.mat_arr)


    def swap(self, row_a, row_b):
        temp = self.mat_arr[row_a]
        self.mat_arr[row_a] = self.mat_arr[row_b]
        self.mat_arr[row_b] = temp

        return Matrix(self.row, self.col, self.mat_arr)


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
