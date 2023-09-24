# Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumu-
# lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

def cumsum(t):
    total = 0
    res = []
    for nested in t:
        total += nested
        res.append(total)
    return res
t = [1, 2, 3]
print(cumsum(t))

# output
# python3 assign10.2/question1.py
# [1, 3, 6]