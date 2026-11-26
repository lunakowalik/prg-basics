def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


for arr in [[1, -9, 9, 11, -3], [-4, -3, -13, 7], [6, 4, -17, 2, -7]]:
    print(bubblesort(arr))