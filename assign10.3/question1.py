# Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

def middle(t):
    return t[1:-1]
t = [1, 2, 3, 4]
print(middle(t))

# output
# python3 assign10.3/question1.py
# [2, 3]