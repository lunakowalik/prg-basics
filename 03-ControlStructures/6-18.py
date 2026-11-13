x = int(input("x = "))
y = int(input("y = "))

if x == 0 and y != 0:
    position = "on the x axis"
elif x != 0 and y == 0:
    position = "on the y axis"
elif x < 0 and y > 0:
    position = "in the first quadrant of the coordinate system"
elif x > 0 and y > 0:
    position = "in the second quadrant of the coordinate system"
elif x > 0 and y < 0:
    position = "in the third quadrant of the coordinate system"
elif x < 0 and y < 0:
    position = "in the fourth quadrant of the coordinate system"
else:
    position = "in position (0) of the coordinate system"

print(f"Point P({x},{y}) is {position}")
