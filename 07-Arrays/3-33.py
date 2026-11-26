arr = [[-38, 19],[5,40],[-7,11],[29,16]]

min_val = arr[0][0]
min_pos = (0, 0)

max_val = arr[0][0]
max_pos = (0, 0)

for r in range(len(arr)):
    for c in range(len(arr[r])):
        val = arr[r][c]
        if val < min_val:
            min_val = val
            min_pos = (r, c)
        if val > max_val:
            max_val = val
            max_pos = (r, c)

print(f"Smallest: {min_val} at row {min_pos[0]}, column {min_pos[1]}")
print(f"Largest: {max_val} at row {max_pos[0]}, column {max_pos[1]}")