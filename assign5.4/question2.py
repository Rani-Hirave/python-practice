# 2.  Write a docstring that explains everything someone would need to know in
#     order to use this function (and nothing else).


def recurse(n, s):
    # Recursive function for getting and printing the value of s;
    # n - positive integer;
    # s - integer.
    
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
recurse(2, 3)
recurse(1, 5)
recurse(0, 6)


# output
# python3 assign5.4/question2.py
# 6
# 6
# 6
# 6
# recurse(-1, 0) will be infinite recursion.
