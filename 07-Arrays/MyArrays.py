def second_largest(arr):
    s = arr[:]
    n = len(s)
    for i in range(n):
        for j in range(0, n - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s[n - 2]


def range_diff(arr):
    mn = arr[0]
    mx = arr[0]
    for x in arr[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mx - mn


def median(arr):
    s = arr[:]
    n = len(s)
    for i in range(n):
        for j in range(0, n - i - 1):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    mid = n // 2
    if n % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def min_max(arr):
    mn = arr[0]
    mx = arr[0]
    for x in arr[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return [mn, mx]


def to_kebab_case(arr):
    res = ""
    for i in range(len(arr)):
        res += str(arr[i])
        if i < len(arr) - 1:
            res += "-"
    return res