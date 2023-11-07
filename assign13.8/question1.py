# Exercise 13.8. Markov analysis:
# 1. Write a program to read a text from a file and perform Markov analysis. The result should be
# a dictionary that maps from prefixes to a collection of possible suffixes. The collection might
# be a list, tuple, or dictionary; it is up to you to make an appropriate choice. You can test your
# program with prefix length two, but you should write the program in a way that makes it easy
# to try other lengths.
# 2. Add a function to the previous program to generate random text based on the Markov analysis.
# Here is an example from Emma with prefix length 2:
# He was very clever, be it sweetness or be angry, ashamed or only amused, at such
# a stroke. She had never thought of Hannah till you were never meant for me?" "I
# cannot make speeches, Emma:" he soon cut it all himself.
# For this example, I left the punctuation attached to the words. The result is almost syntacti-
# cally correct, but not quite. Semantically, it almost makes sense, but not quite.
# What happens if you increase the prefix length? Does the random text make more sense?
# 3. Once your program is working, you might want to try a mash-up: if you combine text from
# two or more books, the random text you generate will blend the vocabulary and phrases from
# the sources in interesting ways.
# Credit: This case study is based on an example from Kernighan and Pike, The Practice of Pro-
# gramming, Addison-Wesley, 1999.
# You should attempt this exercise before you go on; then you can download my so-
# lution from http://thinkpython2.com/code/markov.py . You will also need http://
# thinkpython2.com/code/emma.txt .


import random, string

def import_book(filename, start_line):
    with open("assign13.8/{}".format(filename), "r") as f:
        book_string = str()
        for i in range(start_line):
            next(f)
        for line in f:
            book_string += line
        return book_string

def parse_book(text):
    no_punc = text.translate(text.maketrans("", "", string.punctuation))
    parsed = no_punc.lower().strip().split()
    return parsed

def create_markov_map(word_list, prefix_length=2):
    markov_map = dict()
    current_prefix = tuple()
    for word in word_list:
        if len(current_prefix) == prefix_length:
            markov_map[current_prefix] = markov_map.get(current_prefix, [])
            markov_map[current_prefix].append(word)
            current_prefix = current_prefix[1:] + (word,)
        else:
            current_prefix += word,
    return markov_map

def create_markov_chain(map, length=100):
    markov_chain = str()
    seed = random.choice(list(markov_map.keys()))
    for i in range(length):
        suffixes = markov_map.get(seed, None)
        word = random.choice(suffixes)
        markov_chain += word + " "
        seed = seed[1:] + (word,)
    return markov_chain

emma = import_book("words.txt", 248)
book_words = parse_book(emma)
markov_map = create_markov_map(book_words, 4)
print(create_markov_chain(markov_map))

# output
# python3 assign13.8/question1.py
# spirits required support he was a nervous man easily depressed fond of every body that he was used to and hating to part with them hating change of every kind matrimony as the origin of change was always disagreeable and he was by no means yet reconciled to his own daughters marrying nor could ever speak of her but with compassion though it had been entirely a match of affection when he was now obliged to part with miss taylor too and from his habits of gentle selfishness and of being never able to suppose that other people could feel
