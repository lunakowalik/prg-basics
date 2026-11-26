def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transposed = []

    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(m[r][c])
        transposed.append(new_row)

    return transposed


def print_grid(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()


matrices = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ],
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0],
    ],
    [
        [5, 6, 7, 8],
    ],
]

for idx, mat in enumerate(matrices, start=1):
    print(f"Transposed matrix {idx}:")
    t_mat = transpose_matrix(mat)
    print_grid(t_mat)
    print()