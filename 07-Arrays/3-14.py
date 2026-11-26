arr = [2, 3, 2, 5, 8, 1, 9, 8]
unique = []

for x in arr:
    if arr.count(x) == 1:
        unique.append(x)

print("Array:", *arr)
print("Unique elements:", *unique)