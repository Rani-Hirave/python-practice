# Exercise 13.5. Write a function named choose_from_hist that takes a histogram as defined in
# Section 11.2 and returns a random value from the histogram, chosen with probability in proportion
# to frequency. For example, for this histogram:
#     >>> t = ['a', 'a', 'b']
# >>> hist = histogram(t)
# >>> hist
# {'a': 2, 'b': 1}
# your function should return 'a' with probability 2/3 and 'b' with probability 1/3.

import random

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(hist):
    p = list()
    for key, value in hist.items():
        for i in range(value):
            p.append(key)
    return random.choice(p)

t = ['a', 'a', 'b']
hist = histogram(t)
print(choose_from_hist(hist))

# output
# python3 assign13.5/question1.py
# b