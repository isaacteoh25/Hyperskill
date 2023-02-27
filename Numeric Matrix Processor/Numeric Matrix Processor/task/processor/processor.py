import numpy as np
import itertools

def create_matrix_blueprint(label=""):
    print(f"Enter size of {label}matrix: > ", end='')
    rows, columns = map(int, input().split('\n')[0].split())
    print(f"Enter {label} matrix:")
    mat = []
    # counter to create an empty matrix
    i = 0
    while rows != 0:
        numbers = input().split()
        if len(numbers) != columns:
            pass
        else:
            mat.append([])
            for elements in numbers:
                if elements.isdigit():
                    mat[i].append(int(elements))
                elif str(-1 * float(elements)).isdigit():
                    mat[i].append(int(elements))
                else:
                    mat[i].append(float(elements))

            i += 1
            rows -= 1
    return mat


def add(matrix1, matrix2, rows1, rows2, columns1, columns2):
    add_res = []
    # self = matrix1, other = matrix 2
    if rows1 != rows2 and columns1 != columns2:
        return None
    else:
        for i in range(len(matrix1)):
            for elements in range(len(matrix1[i])):
                add_res.append(matrix1[i][elements] + matrix2[i][elements])
        return add_res


def mul_constant(matrix1):
    mult_constant = []
    number = input("Enter constant: > ")
    if number.isdigit():
        mul_number = int(number)
    else:
        mul_number = float(number)
    for i, j in enumerate(matrix1):
        for elements in j:
            mult_constant.append(mul_number * elements)
    return mult_constant

def mul_mat(matrix1, matrix2, rows1, rows2, columns1, columns2):
    mul_matrices = []
    # self = matrix1, other = matrix 2
    if columns1 == rows2:

        mul = []
        mul1 = []

        """
        Test matrix:
        matrix1 = [[1, 4, 5, 6, 6], [7, 8, 9, 0, 0], [4, 1, 2, 2, 2]]
        matrix2 = [[4, 5], [6, 1], [6, 0], [0, 9], [7, 7]]
        """

        for i in range(len(matrix1)):  # 3
            for k in range(len(matrix2[0])):  # 2
                for j in range(len(matrix2)):  # 5
                    mul.append([matrix1[i][j], matrix2[j][k]])
                    mul1.append(matrix1[i][j] * matrix2[j][k])
        # print(mul)
        # print(mul1)

        # add the results
        for i in range(0, len(mul1), len(matrix1[0])):
            mul_matrices.append(sum(mul1[i:i + len(matrix1[0])]))
        return mul_matrices
    else:
        return None


def transpose_choice():
    choices = input(
        "1. Main diagonal\n"
        "2. Side diagonal\n"
        "3. Vertical line\n"
        "4. Horizontal line\n"
        "Your choice: > \n"
    )
    if choices == '1':
        matrix = create_matrix_blueprint()
        output = main_diagonal(matrix)
        print_output(output, len(matrix))

    elif choices == '2':
        matrix = create_matrix_blueprint()
        output = side_diagonal(matrix)
        print_output(output, len(matrix))

    elif choices == '3':
        matrix = create_matrix_blueprint()
        output = vertical_line(matrix)
        print_output(output, len(matrix))

    elif choices == '4':
        matrix = create_matrix_blueprint()
        output = horizontal_line(matrix)
        print_output(output, len(matrix))
def main_diagonal(matrix):
    # transposing matrix
    # method 1
    # new_matrix = []
    # for i in range(len(matrix[0])):
    #     new_matrix.append([])
    # for i, j in enumerate(matrix):
    #     for k, l in enumerate(j):
    #         new_matrix[k].append(l)
    #
    # new_mat = []
    # for i, j in enumerate(new_matrix):
    #     for elements in j:
    #         new_mat.append(elements)
    # return new_mat

    # method 2
    new_matrix = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_matrix.append(matrix[j][i])
    return new_matrix
def side_diagonal(matrix):
    # method 1
    output = main_diagonal(matrix)
    output.reverse()
    return output

    # # method 2
    # new_matrix = []
    # for i in range(len(matrix) - 1, -1, -1):
    #     for j in range(len(matrix[i]) - 1, -1, -1):
    #         new_matrix.append(matrix[j][i])
    # return new_matrix


def vertical_line(matrix):
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    new_matrix = []
    for i, j in enumerate(matrix):
        j.reverse()
        for elements in j:
            new_matrix.append(elements)
    return new_matrix

def horizontal_line(matrix):
    matrix.reverse()
    new_mat = []
    for i, j in enumerate(matrix):
        for elements in j:
            new_mat.append(elements)
    return new_mat


def print_output(output, columns2):
    if output is None:
        print("The operation cannot be performed.")
    else:
        print("The result is:")
        for all_elements in range(0, len(output), columns2):
            print(*output[all_elements:all_elements + columns2])

    print()


def det_calc(matrix1):
    a = np.array(matrix1)
    return np.linalg.det(a)
    # return mult_constant


def inverse(matrix1):
    try:
        # inverse = numpy.linalg.inv(x)
        y = np.linalg.inv(matrix1)
        return y
    except np.linalg.LinAlgError:
        print("This matrix doesn't have an inverse.")
    # x = np.array(matrix1)



def main():
    matrix_calc = True
    while matrix_calc:
        user_input = input("1. Add matrices\n"
                           "2. Multiply matrix by a constant\n"
                           "3. Multiply matrices\n"
                           "4. Transpose matrix\n"
                           "5. Calculate a determinant\n"
                           "6. Inverse matrix\n"
                           "0. Exit\n"
                           "Your choice: > ")
        if user_input == '1':

            matrix1 = create_matrix_blueprint(label="first ")
            matrix2 = create_matrix_blueprint(label="second ")

            output = add(
                matrix1, matrix2,
                rows1=len(matrix1),
                rows2=len(matrix2),
                columns1=len(matrix1[0]),
                columns2=len(matrix2[0])
            )
            print_output(output, columns2=len(matrix2[0]))
        if user_input == '2':
            matrix = create_matrix_blueprint()
            output = mul_constant(matrix)
            print_output(output, len(matrix[0]))

        if user_input == '3':
            matrix1 = create_matrix_blueprint(label="first ")
            matrix2 = create_matrix_blueprint(label="second ")
            output = mul_mat(
                matrix1, matrix2,
                rows1=len(matrix1),
                rows2=len(matrix2),
                columns1=len(matrix1[0]),
                columns2=len(matrix2[0])
            )
            print_output(output, columns2=len(matrix2[0]))

        if user_input == '4':
            transpose_choice()
        if user_input == '5':
            matrix = create_matrix_blueprint()
            output = det_calc(matrix)
            print("The result is:")
            print(output)
            # print_output(output, len(matrix[0]))
        if user_input == '6':
            matrix = create_matrix_blueprint()
            output = inverse(matrix)
            items = list(itertools.chain.from_iterable(output))
            print_output(items, len(matrix))
        if user_input == '0':
            matrix_calc = False

main()

# import itertools
#
#
# class Matrix:
#     def __init__(self, r, c, items= None):
#         self.row = r
#         self.column = c
#         # items = list(itertools.chain.from_iterable(val))
#         self.cells = [[0 for col in range(c)] for row in range(r)]
#         if items is not None:
#             for i in range(len(items)): self.cells[i // c][i % c] = float(items[i])
#
#     def __getattr__(self, attr):
#         if (attr == "NRows"):
#             return len(self.cells)
#         elif (attr == "NCols"):
#             return len(self.cells[0])
#
#     # def Add(self,rhs):
#     def __add__(self, rhs):
#         try:
#         # if (self.NCols != rhs.NCols) or (self.NRows != rhs.NRows): raise Exception("ERROR")
#             m = Matrix(self.NRows, rhs.NCols)
#             for r in range(m.NRows):
#                 for c in range(m.NCols): m.cells[r][c] = self.cells[r][c] + rhs.cells[r][c]
#             print("The result is:")
#             print(m)
#         except:
#             print('The operation cannot be performed.\n')
#     def multiply(self, rhs ):
#         # m = Matrix(self.row, self.column)
#         m = Matrix(self.row, self.column)
#         for r in range(self.row):
#             for c in range(self.column):
#                 m.cells[r][c] = float(self.cells[r][c]) * float(rhs)
#         print("The result is:")
#         print(m)
#     def __mul__(self, rhs):
#         try:
#             if (self.NCols!=rhs.NRows): raise Exception("Cannot multiply")
#
#             m=Matrix(self.NRows,rhs.NCols)
#             for r in range(m.NRows):
#                 for c in range(m.NCols):
#                     for i in range(self.NCols): m.cells[r][c]+=self.cells[r][i]* rhs.cells[i][c]
#             print("The result is:")
#             print(m)
#         except:
#             print('The operation cannot be performed.\n')
#
#     def __invert__(self):
#         try:
#             m = Matrix(self.NCols, self.NRows)
#             for r in range(m.NRows):
#                 for c in range(m.NCols):
#                     m.cells[r][c]=self.cells[c][r]
#             print(m)
#         except:
#             print('The operation cannot be performed.\n')
#
#     def __sideinvert__(self):
#         try:
#             m = Matrix(self.NCols, self.NRows)
#             for r in range(m.NRows):
#                 for c in range(m.NCols):
#                     m.cells[c][r]=self.cells[r][c]
#             print(m)
#         except:
#             print('The operation cannot be performed.\n')
#
#     def __horizinvert__(self):
#         try:
#             m = Matrix(self.NRows, self.NCols)
#             for r in reversed(range(m.NRows)):
#                 for c in range(m.NCols):
#                     m.cells[c][r]=self.cells[r][c]
#             print(m)
#         except:
#             print('The operation cannot be performed.\n')
#
#     def __vertinvert__(self):
#         try:
#             m = Matrix(self.NRows, self.NCols)
#             for r in range(m.NRows):
#                 for c in reversed(range(m.NCols)):
#                     m.cells[c][r]=self.cells[r][c]
#             print(m)
#         except:
#             print('The operation cannot be performed.\n')
#
#     def __ne__(self, rhs) -> bool:
#         return not (self == rhs)
#
#     def __str__(self):
#         s = ""
#         for r in range(self.NRows):
#             for c in range(self.NCols): s += str(self.cells[r][c]) + " "
#             s += "\n"
#         return s
#
#     # def show(self):
#     #     print(self )
#
# class Menu:
#
#     def main_menu(self):
#         global inp
#         try:
#         # if self.state == 0:
#             print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit\n")
#             # else:
#             #     print("1. Balance\n2. Log out\n0. Exit\n""")
#             inp = int(input())
#         except:
#             print('The operation cannot be performed.\n')
#
#     def Add(self):
#         r, c = map(int, input("Enter size of first matrix:").split())
#         print("Enter first matrix:")
#         menu = [input().split() for i in range(r)]
#         items = list(itertools.chain.from_iterable(menu))
#         mA = Matrix(r, c, items)
#         r1, c1 = map(int, input("Enter size of second matrix:").split())
#         print("Enter second matrix:")
#         matrix1 = [input().split() for i in range(r1)]
#         items1 = list(itertools.chain.from_iterable(matrix1))
#         mB = Matrix(r1,c1, items1)
#         mA.__add__(mB)
#
#
#     def MultiplyCon(self):
#         r, c = map(int, input("Enter size of matrix:").split())
#         # # items = map(int,input().split())
#         menu = [input("Enter matrix:").split() for i in range(r)]
#         items = list(itertools.chain.from_iterable(menu))
#         mul = input("Enter constant:")
#         a = Matrix(r, c, items)
#         a.multiply(mul)
#
#     def Multiply(self):
#         r, c = map(int, input("Enter size of first matrix:").split())
#         print("Enter first matrix:")
#         menu = [input().split() for i in range(r)]
#         items = list(itertools.chain.from_iterable(menu))
#         mA = Matrix(r, c, items)
#         r1, c1 = map(int, input("Enter size of second matrix:").split())
#         print("Enter second matrix:")
#         matrix1 = [input().split() for i in range(r1)]
#         items1 = list(itertools.chain.from_iterable(matrix1))
#         mB = Matrix(r1, c1, items1)
#         mA.__mul__(mB)
#
#     # def logout(self):
#     #     # print("\nYou have successfully logged out!\n")
#     #     self.state = 0
#     def Transpose(self):
#         # diagonal = input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
#         # if diagonal ==1:
#         r,c=3,3
#         items = [1,2,3,4,5,6,7,8,9]
#         # r, c = map(int, input("Enter size of first matrix:").split())
#         # print("Enter matrix:")
#         # menu = [input().split() for i in range(r)]
#         # items = list(itertools.chain.from_iterable(menu))
#         mA = Matrix(r, c, items)
#         # Main diagonal
#         mA.__invert__()
#         mA.__sideinvert__()
#         mA.__horizinvert__()
#         mA.__vertinvert__()
#
#
# menu = Menu()
# inp = -1
# while inp != 0:
#     menu.main_menu()
#     if inp == 1:
#         menu.Add()
#     elif inp == 2:
#         menu.MultiplyCon()
#     elif inp == 3:
#         menu.Multiply()
#     elif inp == 4:
#         menu.Transpose()
#     elif inp == 0:
#         break
# # print("\nBye!")