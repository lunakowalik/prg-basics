arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for r in range(len(arr)):
    for c in range(len(arr[r])):
        arr[r][c] = (r + 1) * (c + 1)

for row in arr:
    for val in row:
        print(f"{val:2d}", end=" ")
    print()