# Exercise 11.1. Write a function that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
# check whether a string is in the dictionary.
# If you did Exercise 10.10, you can compare the speed of this implementation with the list in operator
# and the bisection search.

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d


d = dict(a=1, b=2, c=3, z=1)
inverse = histogram(d)

for val in inverse:
    keys = inverse[val]
    print(val, keys)

# output
# python3 assign11.2/question1.py
# a 1
# b 1
# c 1
# z 1