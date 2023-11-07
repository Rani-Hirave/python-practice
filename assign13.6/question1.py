# Exercise 13.6. Python provides a data structure called set that provides many common set
# operations. You can read about them in Section 19.5, or read the documentation at http:
# // docs. python. org/ 3/ library/ stdtypes. html# types-set .
# Write a program that uses set subtraction to find words in the book that are not in the word list.
# Solution: http: // thinkpython2. com/ code/ analyze_ book2. py .


import string

def import_word_list(filename):
    with open("assign13.6/{}".format(filename), "r") as f:
        wl = list()
        for line in f:
            wl.append(line.strip())
        return wl
    
def import_book(filename):
    with open("assign13.6/{}".format(filename), "r") as f:
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

def not_in_list(book_words, word_list):
    return list(set(book_words) - set(word_list))

plato = import_book("words.txt")
word_list = import_word_list("words.txt")
book_words = parse_book(plato)
word_freq = not_in_list(book_words,word_list)
not_in = not_in_list(book_words, word_list)

for word in not_in:
    print(word)

# output
# python3 assign13.6/question1.py
# abat