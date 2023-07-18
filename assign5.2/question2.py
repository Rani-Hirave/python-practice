# 2 Write a function that prompts the user to input values for a , b , c and n , converts them to
# integers, and uses check_fermat to check whether they violate Fermat’s theorem.

def check_fermat(a,b,c,n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, fermat was wrong!")
    else:
        print("No, that doesn't work. You are a LOSER.")


def user_inputs_fermat():
    a = int(input("Pick a number for a\n"))
    b = int(input("Pick a number for b\n"))
    c = int(input("Pick a number for c\n"))
    n = int(input("Pick a number for n\n"))
    check_fermat(a,b,c,n)


user_inputs_fermat()

# output
# python3 assign5.2/question2.py
# Pick a number for a
# 1
# Pick a number for b
# 1
# Pick a number for c
# 1
# Pick a number for n
# 4
# No, that doesn't work. You are a LOSER.