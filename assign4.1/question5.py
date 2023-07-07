# 5. Make a more general version of circle called arc that takes an additional parameter
# angle , which determines what fraction of a circle to draw. angle is in units of degrees,
# so when angle=360 , arc should draw a complete circle.

import turtle
import math
bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 100)
turtle.mainloop()