arr1 = [3, 8, 5]
arr2 = [7, 3, 2, 8, 5, 9]

is_subset = True

for x in arr1:
    found = False
    for y in arr2:
        if x == y:
            found = True
            break
    if not found:
        is_subset = False
        break

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Is subset:", is_subset)