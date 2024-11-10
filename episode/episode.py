from numpy import ndarray


def episodes(matrix: ndarray):
    rows, cols = matrix.shape

    for r in range(rows):
        for c in range(cols):
            print(matrix[r][c])