# Exercise 13.9. The “rank” of a word is its position in a list of words sorted by frequency: the most
# common word has rank 1, the second most common has rank 2, etc.
# Zipf’s law describes a relationship between the ranks and frequencies of words in natural languages
# ( http: // en. wikipedia. org/ wiki/ Zipf's_ law ). Specifically, it predicts that the frequency,
# f , of the word with rank r is:
# f = cr − s
# where s and c are parameters that depend on the language and the text. If you take the logarithm of
# both sides of this equation, you get:
# log f = log c − s log r
# So if you plot log f versus log r, you should get a straight line with slope − s and intercept log c.
# Write a program that reads a text from a file, counts word frequencies, and prints one line for each
# word, in descending order of frequency, with log f and log r. Use the graphing program of your
# choice to plot the results and check whether they form a straight line. Can you estimate the value of
# s?
# Solution: http: // thinkpython2. com/ code/ zipf. py . To run my solution, you need the plot-
# ting module matplotlib . If you installed Anaconda, you already have matplotlib ; otherwise you
# might have to install it.

import sys
import string

import matplotlib.pyplot as plt

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_line(line, hist):
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace
    for word in line.split():
        word = word.strip(strippables)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def process_file(filename, skip_header):
    hist = {}
    fp = open(filename)
    if skip_header:
        skip_gutenberg_header(fp)
    for line in fp:
        if line.startswith('*** END OF THIS'):
            break
        process_line(line, hist)
    return hist

def rank_freq(hist):
    freqs = list(hist.values())
    freqs.sort(reverse=True)
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()

def main(script, filename='assign13.9/words.txt', flag='plot'):
    hist = process_file(filename, skip_header=True)
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')

if __name__ == '__main__':
    main(*sys.argv)
# output
# python3 assign13.9/question1.py
