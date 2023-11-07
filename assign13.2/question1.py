# Exercise 13.2. Go to Project Gutenberg ( http: // gutenberg. org ) and download your favorite
# out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you downloaded, skip over the
# header information at the beginning of the file, and process the rest of the words as before.
# Then modify the program to count the total number of words in the book, and the number of times
# each word is used.
# Print the number of different words used in the book. Compare different books by different authors,
# written in different eras. Which author uses the most extensive vocabulary?


import string

def import_book(filename):
    with open("assign13.2/{}".format(filename), "r") as f:
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


plato = import_book("words.txt")
word_list = parse_book(plato)
word_freq = word_frequency(word_list)
print("total words: {}".format(len(word_list)))
print(word_freq)
print("different words: {}".format(len(word_freq)))

# output
# python3 assign13.2/question1.py
# total words: 38
# {'abaca': 1, 'abacas': 1, 'abaci': 1, 'aback': 1, 'abacus': 1, 'abacuses': 1, 'abaft': 1, 'abaka': 1, 'abakas': 1, 'abalone': 1, 'abalones': 1, 'abamp': 1, 'abampere': 1, 'abamperes': 1, 'abamps': 1, 'abandon': 1, 'abandoned': 1, 'abandoning': 1, 'abandonment': 1, 'abandonments': 1, 'abandons': 1, 'abas': 1, 'abase': 1, 'abased': 1, 'abasedly': 1, 'abasement': 1, 'abasements': 1, 'abaser': 1, 'abasers': 1, 'abases': 1, 'abash': 1, 'abashed': 1, 'abashes': 1, 'abashing': 1, 'abasing': 1, 'abatable': 1, 'abate': 1, 'abat': 1}
# different words: 38