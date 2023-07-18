# Exercise 5.4. What is the output of the following program? Draw a stack diagram that shows the
# state of the program when it prints the result.
# def recurse(n, s):
# if n == 0:
# print(s)
# else:
# recurse(n-1, n+s)
# recurse(3, 0)
# 1. What would happen if you called this function like this: recurse(-1, 0) ?

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
recurse(-1, 0)
print()

# output
# python3 assign5.4/question1.py
# 6
# Traceback (most recent call last):
#   File "assign5.4/question1.py", line 18, in <module>
#     recurse(-1, 0)
#   File "assign5.4/question1.py", line 15, in recurse
#     recurse(n-1, n+s)
#   File "assign5.4/question1.py", line 15, in recurse
#     recurse(n-1, n+s)
#   File "assign5.4/question1.py", line 15, in recurse
#     recurse(n-1, n+s)
#   [Previous line repeated 995 more times]
#   File "assign5.4/question1.py", line 12, in recurse
#     if n == 0:
# RecursionError: maximum recursion depth exceeded in comparison