# Exercise 13.4. Modify the previous program to read a word list (see Section 9.1) and then print all
# the words in the book that are not in the word list. How many of them are typos? How many of
# them are common words that should be in the word list, and how many of them are really obscure?

import string

def import_book(filename):
    with open("assign13.4/{}".format(filename), "r") as f:
        book_string = str()
        for i in range(33):
            next(f)
        for line in f:
            book_string += line
        return book_string[:300]
    
def parse_book(text):
    no_punc = text.translate(text.maketrans("", "", string.punctuation))
    parsed = no_punc.lower().strip().split()
    return parsed


def word_frequency(word_list):
    hist = dict()
    for word in word_list:
        hist[word] = hist.get(word, 0) + 1
    return hist

def top_20(word_freq):
    fr = list()
    for word, freq in word_freq.items():
        fr.append((freq, word))
    fr.sort(reverse=True)
    mf = list()
    for (freq, word) in fr:
        mf.append(word)
    return mf[:20]

def import_word_list(filename):
    with open("assign13.4/{}".format(filename), "r") as f:
        wl = list()
        for line in f:
            wl.append(line.strip())
        return wl

def not_in_list(book_words, word_list):
    not_in = list()
    for word in book_words:
        if word not in word_list:
            not_in.append(word)
    return not_in

plato = import_book("words.txt")
word_list = import_word_list("words.txt")
book_words = parse_book(plato)
word_freq = word_frequency(book_words)
top_words = top_20(word_freq)
not_in = not_in_list(book_words, word_list)
for word in not_in:
    print(word)

# output
# python3 assign13.4/question1.py
# abat