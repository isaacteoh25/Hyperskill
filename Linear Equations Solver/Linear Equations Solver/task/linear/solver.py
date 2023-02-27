import argparse
import numpy as np


def transform_matrix(matrix, var, rows):
    for row in range(min((var, rows))):
        if matrix[row][row] == 0.0:
            for rest in range(row + 1, len(matrix)):
                if matrix[rest][row] != 0:
                    a, b = matrix[rest].copy(), matrix[row].copy()
                    matrix[row], matrix[rest] = a, b
                    break
        if matrix[row][row] != 0.0:
            mul = 1 / matrix[row][row]
            matrix[row] *= mul
            for rest in range(row + 1, len(matrix)):
                sub = matrix[rest][row] / matrix[row][row]
                matrix[rest] = matrix[rest] - matrix[row] * sub
        else:
            if matrix[row][:-1].sum() == 0.0 and matrix[row][-1] != 0.0:
                return "No solutions"
    sig_eq = 0
    for row in matrix:
        if row[:-1].sum() != 0.0:
            sig_eq += 1
    if sig_eq < var or var > rows:
        return "Infinitely many solutions"
    for row in matrix:
        if row[:-1].sum() == 0.0 and row[-1] != 0.0:
            return "No solutions"
    return matrix


parser = argparse.ArgumentParser()
parser.add_argument('--infile')
parser.add_argument('--outfile')
args = parser.parse_args()
matrix = []

with open(args.infile, "r", encoding='utf-8') as file:
    var, rows = list(map(int, file.readline().split()))
    content = file.read()
    cmp = True if "j" in content else False
    for row in content.split("\n"):
        matrix.append(row.split(" "))
if cmp:
    matrix = np.array(matrix, dtype=np.complex)
else:
    matrix = np.array(matrix, dtype=np.float64)

matrix = transform_matrix(matrix, var, rows)

with open(args.outfile, "w", encoding='utf-8') as file:
    if isinstance(matrix, str):
        file.write(matrix)
    else:
        for row in range(var - 1, -1, -1):
            for rest in range(row - 1, -1, -1):
                sub = matrix[rest][row] / matrix[row][row]
                matrix[rest] = matrix[rest] - matrix[row] * sub
        for row in range(var):
            file.write(str(matrix[row][len(matrix[row]) - 1]) + "\n")
print(f"Saved to {args.outfile}")