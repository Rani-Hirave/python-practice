# 3. Make a copy of square and change the name to polygon . Add another parameter
# named n and modify the body so it draws an n-sided regular polygon. Hint: The
# exterior angles of an n-sided regular polygon are 360/n degrees.

import turtle
bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 200)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        angle = 360.0/n
        t.lt(angle)
        
polygon(bob,30,15)

turtle.mainloop()
