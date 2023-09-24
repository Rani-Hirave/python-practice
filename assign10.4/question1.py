# Exercise 10.4. Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None . For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]

def chop(t):
    del(t[0])
    del(t[-1])
    return t
t = [1, 2, 3, 4]
print(chop(t))

# output
# python3 assign10.4/question1.py
# [2, 3]