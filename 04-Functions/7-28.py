def f(dice):
    if not dice:
        return None

    best_digit = int(dice[0])
    best_streak = 1

    current_digit = int(dice[0])
    current_streak = 1

    for ch in dice[1:]:
        digit = int(ch)
        if digit == current_digit:
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
                best_digit = current_digit
        else:
            current_digit = digit
            current_streak = 1

    return best_digit


print(f'f("5233165554211") returns {f("5233165554211")}')
print(f'f("2133") returns {f("2133")}')