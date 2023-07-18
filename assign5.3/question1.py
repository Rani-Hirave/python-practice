# If you are given three sticks, you may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not
# be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to
# see if it is possible to form a triangle:
# If any of the three lengths is greater than the sum of the other two, then you cannot
# form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
# form what is called a “degenerate” triangle.)
# 1. Write a function named is_triangle that takes three integers as arguments, and that prints
# either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
# with the given lengths.

def is_triangle(a, b, c):
    if c > (a+b) or b > (a+c) or a > (b+c):
        print('No')
    else:
        print('Yes')

is_triangle(4, 5, 6) 
is_triangle(1, 2, 9) 
print()

# output
# python3 assign5.3/question1.py
# Yes
# No