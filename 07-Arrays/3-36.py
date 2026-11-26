def identity_matrix(n):
    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            if r == c:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix


def print_grid(arr):
    for row in arr:
        for val in row:
            print(val, end=" ")
        print()


for size in [3, 5, 8]:
    print(f"Identity matrix ({size}x{size}):")
    mat = identity_matrix(size)
    print_grid(mat)
    print()