# Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.

def has_duplicates(s):
    t = list(s)
    t.sort()

    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False
print(has_duplicates('cba'))
print(has_duplicates('abba'))


# python3 assign10.7/question1.py
# False
# True