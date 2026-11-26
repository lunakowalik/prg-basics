def f(number):
    digits = str(abs(number))
    total = 0

    for ch in digits:
        if digits.count(ch) > 1:
            total += int(ch)

    return total


print(f'f(1027) returns {f(1027)}')
print(f'f(230335) returns {f(230335)}')
print(f'f(513553007) returns {f(513553007)}')