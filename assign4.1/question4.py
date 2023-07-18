# 4. Write a function called circle that takes a turtle, t , and radius, r , as parameters and
# that draws an approximate circle by calling polygon with an appropriate length and
# number of sides. Test your function with a range of values of r .
# Hint: figure out the circumference of the circle and make sure that length * n =
# circumference .

import turtle
import math

bob = turtle.Turtle()
print(bob)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        angle = 360.0/n
        t.lt(angle)

def circle(t, r):
        circum= 2*math.pi*r
        n= int(circum/10)+1
        length= circum/n
        polygon(t,length, n)

circle(bob, 100)
turtle.mainloop()

# output
# draw circle