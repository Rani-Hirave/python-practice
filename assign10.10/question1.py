# Exercise 10.10. To check whether a word is in the word list, you could use the in operator, but it
# would be slow because it searches through the words in order.
# Because the words are in alphabetical order, we can speed things up with a bisection search (also
# known as binary search), which is similar to what you do when you look a word up in the dictionary
# (the book, not the data structure). You start in the middle and check to see whether the word you are
# looking for comes before the word in the middle of the list. If so, you search the first half of the list
# the same way. Otherwise you search the second half.
# Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will
# take about 17 steps to find the word or conclude that it’s not there.
# Write a function called in_bisect that takes a sorted list and a target value and returns True if
# the word is in the list and False if it’s not.
# Or you could read the documentation of the bisect module and use that! Solution: http: //
# thinkpython2. com/ code/ inlist. py .

import bisect
def make_word_list():
    word_list = []
    fin = open('assign10.10/words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False
    i = len(word_list) // 2
    if word_list[i] == word:
        return True
    if word_list[i] > word:
        return in_bisect(word_list[:i], word)
    else:
        return in_bisect(word_list[i+1:], word)


def in_bisect_cheat(word_list, word):
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False
    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()
    for word in ['aa', 'alien', 'abies']:
        print(word, 'in list', in_bisect(word_list, word))

# python3 assign10.10/question1.py
# aa in list False
# alien in list False
# abies in list True