# Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.
# Hint: The string module provides a string named whitespace , which contains space, tab, new-
# line, etc., and punctuation which contains the punctuation characters. Let’s see if we can make
# Python swear:
# >>> import string
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

import string

def parse(text):
    no_punc = text.translate(text.maketrans('', '', string.punctuation))
    parsed = no_punc.lower().strip().split()
    return parsed
print(parse("bashes abases abase abas aas aa a"))
# output
# python3 assign13.1/question1.py
# ['bashes', 'abases', 'abase', 'abas', 'aas', 'aa', 'a']
