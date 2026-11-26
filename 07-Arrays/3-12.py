arr1 = [4, 36, 12, 28, 9, 44, 5]
arr2 = [5, 1, 36]

for x in arr1:
    found = False
    for y in arr2:
        if x == y:
            found = True
            break
    if not found:
        print(x, end=" ")
print()