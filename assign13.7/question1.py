# Exercise 13.7. Write a program that uses this algorithm to choose a random word from the book.
# Solution: http: // thinkpython2. com/ code/ analyze_ book3. py .


import random, string
from bisect import bisect

def import_book(filename):
    with open("assign13.7/{}".format(filename), "r") as f:
        book_string = str()
        for i in range(33):
            next(f)
        for line in f:
            book_string += line
        return book_string


def parse_book(text):
    no_punc = text.translate(text.maketrans("", "", string.punctuation))
    parsed = no_punc.lower().strip().split()
    return parsed

def word_frequency(word_list):
    hist = dict()
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return hist

def random_word(hist):
    words = list()
    freqs = list()
    total_freq = 0
    for word, freq in hist.items():
        words.append(word)
        total_freq += freq
        freqs.append(total_freq)
    r = random.randint(0, total_freq-1)
    index = bisect(freqs, r)
    return words[index]
emma = import_book("words.txt")
book_words = parse_book(emma)
word_freq = word_frequency(book_words)
for i in range(20):
    print(random_word(word_freq))

# output
# python3 assign13.7/question1.py
# abaca
# abacus
# abas
# abalone
# abaca
# abasedly
# abampere
# abate
# abasement
# abalones
# abaser
# abaft
# abalone
# abamps
# abamp
# abandonments
# abasers
# abandoning
# abased
# abaft