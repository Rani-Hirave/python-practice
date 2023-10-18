# Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates that
# takes a list as a parameter and returns True if there is any object that appears more than once in the
# list.
# Use a dictionary to write a faster, simpler version of has_duplicates . Solution: http: //
# thinkpython2. com/ code/ has_ duplicates. py

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def has_duplicates2(t):
    return len(set(t)) < len(t)

t = [1, 2, 3]
print(has_duplicates(t))
t.append(1)
print(has_duplicates(t))

t = [1, 2, 3]
print(has_duplicates2(t))
t.append(1)
print(has_duplicates2(t))

# output
# python3 assign11.4/question1.py
# False
# True
# False
# True