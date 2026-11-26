def f(number, even):
    total = 0
    num = abs(number)

    while num > 0:
        digit = num % 10
        if even and digit % 2 == 0:
            total += digit
        elif not even and digit % 2 != 0:
            total += digit
        num //= 10

    return total


print(f'f(3124, True) returns {f(3124, True)}')
print(f'f(3124, False) returns {f(3124, False)}')
print(f'f(20576, False) returns {f(20576, False)}')
print(f'f(20576, True) returns {f(20576, True)}')
print(f'f(13115, True) returns {f(13115, True)}')