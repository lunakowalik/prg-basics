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

last_row_idx = len(arr) - 1
arr[0], arr[last_row_idx] = arr[last_row_idx], arr[0]

print("\nAfter:")
print_grid(arr)