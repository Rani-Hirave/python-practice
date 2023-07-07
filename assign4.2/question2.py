# 2. Write an appropriately general set of functions that can draw flowers as in Figure
import math
import turtle

def polyline(obj, length, sides, angle):
    for i in range(sides):
        obj.fd(length)
        obj.lt(angle)

def arc(t, radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    sides = int(arc_length / 3) + 1
    step_length = arc_length / sides
    step_angle = angle / sides

    polyline(t, step_length, sides, step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180.0-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move_turtle(t, length):
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()

move_turtle(bob, -200)
flower(bob, 7, 60.0, 60.0)

move_turtle(bob, 200)
flower(bob, 10, 50.0, 70.0)

move_turtle(bob, 200)
flower(bob, 20, 120.0, 20.0)

bob.hideturtle()
turtle.mainloop()