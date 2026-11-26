import math
import matplotlib.pyplot as plt

x = []
y = []

# create angle values in degrees from 0 to 360
for deg in range(0, 361):
    x = x + [deg]

# compute sin(x) using radians
for deg in x:
    rad = math.radians(deg)
    y = y + [math.sin(rad)]

plt.plot(x, y)
plt.show()