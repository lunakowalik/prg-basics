def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True


pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]

for a, b in pairs:
    print("Array1:", " ".join([str(x) for x in a]))
    print("array2:", " ".join([str(x) for x in b]))
    same = compare(a,b)
    print("Comparison:", "arrays are" + "" if same else "not " + "the same")
    print()