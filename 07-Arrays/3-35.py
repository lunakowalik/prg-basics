arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]


def print_grid(grid):
    for row in grid:
        for val in row:
            print(f"{val:2d}", end=" ")
        print()


print("Before:")
print_grid(arr)

for row in arr:
    last_col_idx = len(row) - 1
    row[0], row[last_col_idx] = row[last_col_idx], row[0]

print("\nAfter:")
print_grid(arr)