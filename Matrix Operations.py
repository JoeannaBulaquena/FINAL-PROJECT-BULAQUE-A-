import numpy as np

# 1. Transpose the given input of 3x4 matrix
def transpose_matrix(matrix):
    transposed = np.transpose(matrix)
    print("Transposed matrix:")
    print(transposed)

matrix_3x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
transpose_matrix(matrix_3x4)

# 2. Find the sum of rows and columns of elements using numpy
def sum_rows_columns(matrix):
    matrix_np = np.array(matrix)
    sum_rows = np.sum(matrix_np, axis=1)
    sum_columns = np.sum(matrix_np, axis=0)
    print(f"Sum of rows: {sum_rows}")
    print(f"Sum of columns: {sum_columns}")

sum_rows_columns(matrix_3x4)

# 3. Find the sum of diagonal elements in a given matrix the manual way
def sum_diagonals(matrix):
    size = min(len(matrix), len(matrix[0]))  # For non-square matrices
    primary_diagonal_sum = sum(matrix[i][i] for i in range(size))
    secondary_diagonal_sum = sum(matrix[i][len(matrix[0]) - 1 - i] for i in range(size))
    print(f"Sum of primary diagonal: {primary_diagonal_sum}")
    print(f"Sum of secondary diagonal: {secondary_diagonal_sum}")

sum_diagonals(matrix_3x4)