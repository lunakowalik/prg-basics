def flatten_2d_to_1d(arr):
    result = []
    for row in arr:
        for val in row:
            result.append(val)
    return result


arrays_2d = [
    [
        [2, 3],
        [1, 5],
    ],
    [
        [5, 0, 3, 7, 5],
        [9, 0, 9, 1, 2],
    ],
    [
        [2, 1],
        [3, 5],
        [7, 4],
        [2, 6],
    ],
]

for idx, grid in enumerate(arrays_2d, start=1):
    flat = flatten_2d_to_1d(grid)
    print(f"1D array {idx}:", flat)