# 1. Draw a stack diagram that shows the state of the program while executing circle(bob,
# radius) . You can do the arithmetic by hand or add print statements to the code.
# 2. The version of arc in Section 4.7 is not very accurate because the linear approximation of the
# circle is always outside the true circle. As a result, the Turtle ends up a few pixels away from
# the correct destination. My solution shows a way to reduce the effect of this error. Read the
# code and see if it makes sense to you. If you draw a diagram, you might see how it works.

import turtle
import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def circle(t, r):
    arc(t, r, 360)


bob = turtle.Turtle()
radius = 100

bob.pu()
bob.fd(radius)
bob.lt(90)
bob.pd()

circle(bob,radius)
turtle.mainloop()

# output
# draw circle with arc