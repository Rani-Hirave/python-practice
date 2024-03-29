# Exercise 5.6. The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
# curve with length x, all you have to do is
# 1. Draw a Koch curve with length x/3.
# 2. Turn left 60 degrees.
# 3. Draw a Koch curve with length x/3.
# 4. Turn right 120 degrees.
# 5. Draw a Koch curve with length x/3.
# 6. Turn left 60 degrees.
# 7. Draw a Koch curve with length x/3.
# The exception is if x is less than 3: in that case, you can just draw a straight line with length x.
# 1. Write a function called koch that takes a turtle and a length as parameters, and that uses the
# turtle to draw a Koch curve with the given length.
# 2. Write a function called snowflake that draws three Koch curves to make the outline of a
# snowflake.
# Solution: http: // thinkpython2. com/ code/ koch. py .
# 3. The Koch curve can be generalized in several ways. See http: // en. wikipedia. org/
# wiki/ Koch_ snowflake for examples and implement your favorite.

import turtle

def koch(t, n):
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        t.rt(120)

bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()

# output
# draw A Koch curve.