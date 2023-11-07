# Exercise 12.2. More anagrams!
# 1. Write a program that reads a word list from a file (see Section 9.1) and prints all the sets of
# words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a collection of letters to a list
# of words that can be spelled with those letters. The question is, how can you represent the
# collection of letters in a way that can be used as a key?

fin = open("assign12.2/words.txt")

def word_to_tuple(word):
    word = tuple(sorted(word))
    return word


def print_anagrams(anagrams):
    for letter_set in anagrams:
        words = anagrams.get(letter_set)
        if len(words) > 1:
            print(words)


def anagrams(word_list):
    output = dict()
    for word in word_list:
        word = word.strip()
        letters = word_to_tuple(word)
        output[letters] = output.get(letters, [])
        output[letters].append(word)
    return output
print_anagrams(anagrams(fin))

# output
# python3 assign12.2/question1.py
# ['deltas', 'desalt', 'lasted', 'salted', 'staled', 'slated']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']