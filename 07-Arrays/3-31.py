def create_2d_arr(x, y):
    arr = []
    for _ in range(x):
        row = []
        for _ in range(y):
            row.append(0)
        arr.append(row)
    return arr


grid = create_2d_arr(3, 5)

for row in grid:
    for val in row:
        print(val, end=" ")
    print()