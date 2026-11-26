def f(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 1
    b = 0

    for _ in range(3, n + 1):
        c = a + b
        b = a
        a = c

    return a


print(f'f(5) returns {f(5)}')
print(f'f(9) returns {f(9)}')