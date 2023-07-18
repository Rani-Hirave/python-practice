# 3. Write an appropriately general set of functions that can draw shapes as in Figure 4.2.

# from __future__ import print_function, division

import math
import turtle

def draw_pie(t, n, r):
    draw_poly_pie(t, n, r)
    t.pu()
    t.fd(r*2 + 10)
    t.pd()

def draw_poly_pie(t, n, r):
    interior_angle = 360/n
    for i in range(n):
        draw_triangle(t, r, interior_angle/2)
        t.lt(180 + interior_angle/2)

def draw_triangle(t, r, angle):    
    y = 2 * r * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(y)
    t.lt(90 + angle)
    t.fd(r)

bob = turtle.Turtle()

bob.pu()
bob.bk(130)
bob.pd()

size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)

bob.hideturtle()
turtle.mainloop()

# output
# draw flower with pipe