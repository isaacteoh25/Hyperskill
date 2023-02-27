# Numeric Matrix Processor (without using array or NumPy etc)

# ==============================
# input a matrix by specifying the size, type of numbers, and the rows of numbers
def enter_matrix(label='', kind=int):  # say kind=float if needed
    r1, c1 = map(int, input('Enter size of {}{}matrix:'.format(label, '' if label == '' else ' ')).split())
    print('Enter {}{}matrix:'.format(label, ' ' if label != '' else ''))
    return [list(map(kind, input().split())) for _r in range(r1)]

# ==============================
#   sum of products
def sum_of_products(l1, l2):  # a row of first matrix and a column of the second
    if len(l1) != len(l2):  # both vectors l1 and l2 must be same length)
        print('input vectors not same length')
        return
    sum = 0
    for i in range(len(l1)):
        sum += l1[i] * l2[i]
    return sum

# ==============================
# Matrix scale (multiply by number)
def matrix_scale():
    matrix1 = enter_matrix(kind=float)

    multiplier = float(input('Enter constant:'))

    result = [[item * multiplier for item in row] for row in matrix1]
    print('The result is:')
    for row in result:  # alternatively if I won't need to use result later,
        print(*row)     # just put that expression in place of result


# ==============================
# Matrix addition
def matrix_add():
    matrix1 = enter_matrix(label='first', kind=float)
    matrix2 = enter_matrix(label='second', kind=float)
    r1 = len(matrix1)
    c1 = len(matrix1[0])
    if r1 != len(matrix2) or c1 != len(matrix2[0]):
        print('The operation cannot be performed.')
        return

    matrix3 = [list(matrix2[r][c] + matrix1[r][c] for c in range(c1)) for r in range(r1)]
    print('The result is:')
    for row in matrix3:
        print(*row)
    return


# ==============================
# Matrix multiplication (dot product)
def matrix_multiply():
    matrix1 = enter_matrix(label='first', kind=float)
    matrix2 = enter_matrix(label='second', kind=float)
    # building matrix3 seems to be needed if I want to address the resulting matrix with index numbers
    # other options are to use matrix3.append(...   or matrix3.insert(...
    # result matrix will have the # rows of matrix1 and # columns of matrix2
    matrix3 = [[0 for _j in range(len(matrix2[0]))] for _i in range(len(matrix1))]  # [[c2] then r1]
    # print(matrix3)

    for i in range(len(matrix1)):  # r1
        l1 = matrix1[i]  # a row of matrix1
        for j in range(len(matrix2[0])):  # c2
            l2 = [matrix2[x][j] for x in range(len(matrix2))]  # a column of matrix2
            value = sum_of_products(l1, l2)
            matrix3[i][j] = value  # this value goes in matrix3[i][j]
            # print('({},{}) -> {}'.format(i, j, value))
    print('The result is:')
    for row in matrix3:
        print(*row)


# ==============================
# Matrix transpose - 4 ways
def matrix_transpose():
    t_choice = int(input('''\n1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
Your choice: '''))
    matrix1 = enter_matrix(kind=float)  # assume integer
    matrix3 = [[]]
    # matrix must be square, n by n
    if len(matrix1) != len(matrix1[0]):
        print('Error - matrix is not square')
        return
    n = len(matrix1)  # number of rows and thus columns

    if t_choice == 1:  # transpose around the main diagonal (count columns first)
        matrix3 = [[matrix1[c][r] for c in range(n)] for r in range(n)]

    elif t_choice == 2:  # transpose around the side diagonal (count backwards on both indices)
        matrix3 =[[matrix1[r][c] for r in range(n - 1, -1, -1)]for c in range(n - 1, -1, -1)]
#                [[matrix1[r][c] for r in reversed(range(n))] for c in reversed(range(n))]

    elif t_choice == 3:  # transpose around the vertical line (count backwards on columns first)
        matrix3 = [[matrix1[r][c] for c in range(n - 1, -1, -1)]for r in range(4)]
#                 [[matrix1[r][c] for c in reversed(range(n))]for r in range(4)]

    elif t_choice == 4:  # transpose around the horizontal line (count backwards on rows second)
        matrix3 = [[matrix1[r][c] for c in range(4)]for r in range(n - 1, -1, -1)]
#                 [[matrix1[r][c] for c in range(4)]for r in reversed(range(n))]

    else:
        print('invalid entry')
        # do nothing to go back and try again or   return to give up in disgust
    print('The result is:')
    for row in matrix3:
        print(*row)
    return
# ============== DETERMINANT ============
def get_minor(mat_in, r_in, c_in):  # return matrix mat_in without row r_in and column c_in
    s = len(mat_in)
    return [[mat_in[r][c] for c in range(s) if c != c_in]for r in range(s) if r != r_in]
    #                      \_____ column numbers _____/   \_______ row numbers ______/


def get_cofactor(r_in, c_in):  # return +1 or -1 depending on where r_in and c_in are
    return 1 if (r_in + c_in) % 2 == 0 else -1


def compute_determinant(z):
    if len(z) == 2:  # this is the base case for a 2x2
        return(z[0][0] * z[1][1] - z[0][1] * z[1][0])
    if len(z) == 1:  # for a 1x1 it is just the single value
        return z[0][0]
    accumulator = 0
    for x in range(len(z[0])):  # x is the column number in row 0
        new_matrix = get_minor(z, 0, x)
        accumulator += z[0][x] * get_cofactor(0, x) * compute_determinant(new_matrix)
    return accumulator


def get_determinant():
    matrix1 = enter_matrix(kind=float)
    print(compute_determinant(matrix1))


# ============== Inverse ============
def make_adjoint(t):  # cofactor * det(minor) ONLY. Do not multiply by element that produces minor
    n = len(t)  # no of rows = no of columns (square matrix)
    return [[get_cofactor(r, c) * compute_determinant(get_minor(t, r, c)) for r in range(n)] for c in range(n)]


def make_inverse():  # matrix is square - get it then invert it
    matrix1 = enter_matrix(kind=float)
    det = compute_determinant(matrix1)
    adj = make_adjoint(matrix1)
    inv = [[item / det for item in row] for row in adj]  # scale by constant = 1/det
    print('The result is:')
    for row in inv:
        for item in row:
            print('{:-7.3f} '.format(item), end='')
        print()
    return
# ============== MAIN ============

while True:
    choice = int(input('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice:'''))
    if choice == 1:
        matrix_add()
    elif choice == 2:
        matrix_scale()
    elif choice == 3:
        matrix_multiply()
    elif choice == 4:
        matrix_transpose()
    elif choice == 5:
        get_determinant()
    elif choice == 6:
        make_inverse()
    elif choice == 0:
        break
    else:
        print('invalid entry')
    print()