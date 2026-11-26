import turtle


def draw_square(pen, length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)


def draw_trangle(pen, length):
    # Closed triangle with two equal legs of length * 0.7071
    pen.forward(length)
    pen.left(135)
    pen.forward(length * 0.7071)
    pen.left(90)
    pen.forward(length * 0.7071)
    pen.right(135)


def draw_rectangle(pen, lenght_a, lenght_b):
    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)