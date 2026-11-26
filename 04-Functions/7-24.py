def f(expression):
    if not expression:
        return 0

    total = 0
    sign = 1

    for ch in expression:
        if ch == "+":
            sign = 1
        elif ch == "-":
            sign = -1
        elif ch.isdigit():
            total += sign * int(ch)

    return total


print(f'f("2+3") returns {f("2+3")}')
print(f'f("3+8+1") returns {f("3+8+1")}')
print(f'f("2+3-4+5-0") returns {f("2+3-4+5-0")}')