# Exercise 5.5. Read the following function and see if you can figure out what it does (see the exam-
# ples in Chapter 4). Then run it and see if you got it right.

import turtle
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob = turtle.Turtle()
draw(bob, 10, 5)    
turtle.mainloop()

# output
# draw A Koch curve.