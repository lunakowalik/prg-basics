matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

n = len(matrix)

for r in range(n):
    for c in range(n):
        if r == c:
            matrix[r][c] = 1

# Print formatted matrix
for row in matrix:
    print(" ".join(str(val) for val in row))