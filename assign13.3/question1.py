# Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently used
# words in the book.

import string

def import_book(filename):
    with open("assign13.3/{}".format(filename), "r") as f:
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

plato = import_book("words.txt")
word_list = parse_book(plato)
word_freq = word_frequency(word_list)
top_words = top_20(word_freq)

for word in top_words:
    print(word)

# output
# python3 assign13.3/question1.py
# abate
# abatable
# abat
# abasing
# abashing
# abashes
# abashed
# abash
# abases
# abasers
# abaser
# abasements
# abasement
# abasedly
# abased
# abase
# abas
# abandons
# abandonments
# abandonment