def f(detector):
    people = 0
    for event in detector:
        if event == "+":
            people += 1
        elif event == "-":
            people -= 1

        if people >= 3:
            return True

    return False


print(f'f("+-+++-+---") returns {f("+-+++-+---")}')
print(f'f("+-+-+-+-") returns {f("+-+-+-+-")}')
print(f'f("+-++-+--") returns {f("+-++-+--")}')
print(f'f("+-++-++-+---") returns {f("+-++-++-+---")}')