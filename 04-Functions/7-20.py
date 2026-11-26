def is_prime(num):
    if num < 2:
        return False
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            return False
    return True


def f(n):
    if n <= 0:
        return None

    count = 0
    candidate = 1

    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1

    return candidate


print(f'f(1) returns {f(1)}')
print(f'f(5) returns {f(5)}')