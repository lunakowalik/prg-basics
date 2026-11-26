###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)


def move_to(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


# Draw figures
move_to(-260, 180)
figures.draw_square(pen, 80)

move_to(120, 180)
figures.draw_square(pen, 60)

move_to(-260, -20)
figures.draw_trangle(pen, 90)

move_to(120, -20)
figures.draw_trangle(pen, 70)

move_to(-260, -180)
figures.draw_rectangle(pen, 110, 50)

move_to(120, -180)
figures.draw_rectangle(pen, 90, 45)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()