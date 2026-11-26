def f(amount_to_pay):
    coins = 0

    coins += amount_to_pay // 5
    amount_to_pay = amount_to_pay % 5

    coins += amount_to_pay // 2
    amount_to_pay = amount_to_pay % 2

    coins += amount_to_pay

    return coins


print(f'f(23) returns {f(23)}')
print(f'f(8) returns {f(8)}')
print(f'f(2) returns {f(2)}')
print(f'f(0) returns {f(0)}')