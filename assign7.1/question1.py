# Exercise 7.1. Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that
# takes a as a parameter, chooses a reasonable value of x , and returns an estimate of the square root of
# a .
# To test it, write a function named test_square_root that prints a table like this:
# a
# mysqrt(a)
# math.sqrt(a) diff
# -
# ---------
# ------------ ----
# 1.0 1.0
# 1.0
# 0.0
# 2.0 1.41421356237 1.41421356237 2.22044604925e-16
# 3.0 1.73205080757 1.73205080757 0.0
# 4.0 2.0
# 2.0
# 0.0
# 5.0 2.2360679775 2.2360679775 0.0
# 6.0 2.44948974278 2.44948974278 0.0
# 7.0 2.64575131106 2.64575131106 0.0
# 8.0 2.82842712475 2.82842712475 4.4408920985e-16
# 9.0 3.0
# 3.0
# 0.0
# The first column is a number, a; the second column is the square root of a computed with mysqrt ;
# the third column is the square root computed by math.sqrt ; the fourth column is the absolute value
# of the difference between the two estimates.

import math

def mysqrt(a):
    x = a/2
    while True:
        estimated_root = (x + a/x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root

def test_square_root(list_of_a):
    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"
    
    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""
    
    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    
    for a in list_of_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)

test_square_root(range(1,10))


# output
# python3 assign7.1/question1.py
# a   mysqrt(a)     math.sqrt(a)  diff
# 1.0 1.000000      1.000000      0.0
# 2.0 1.414214      1.414214      2.220446049250313e-16
# 3.0 1.732051      1.732051      0.0
# 4.0 2.000000      2.000000      0.0
# 5.0 2.236068      2.236068      0.0
# 6.0 2.449490      2.449490      0.0
# 7.0 2.645751      2.645751      0.0
# 8.0 2.828427      2.828427      4.440892098500626e-16
# 9.0 3.000000      3.000000      0.0