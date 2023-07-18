# Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
# a n + b n = c n
# for any values of n greater than 2.
# 1. Write a function named check_fermat that takes four parameters— a , b , c and n —and
# checks to see if Fermat’s theorem holds. If n is greater than 2 and
# a n + b n = c n
# the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
# print, “No, that doesn’t work.”

def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, fermat was wrong!")
    else:
        print("No, that doesn't work. You are a LOSER.")

check_fermat(1,2,3,3)
check_fermat(0,0,0,3)

# output
# python3 assign5.2/question1.py
# No, that doesn't work. You are a LOSER.
# Holy smokes, fermat was wrong!
