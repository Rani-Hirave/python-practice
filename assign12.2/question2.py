# Exercise 12.2. More anagrams!
# 2. Modify the previous program so that it prints the longest list of anagrams first, followed by
# the second longest, and so on.

fin = open("assign12.2/words.txt")

def word_to_tuple(word):
    word = tuple(sorted(word))
    return word


def print_anagrams(anagrams):
    sorted_words = list()
    for letter_set in anagrams:
        words = anagrams.get(letter_set)
        if len(words) > 1:
            sorted_words.append(words)
    for set in sorted(sorted_words, key=len, reverse=True):
        print(set)


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
# python3 assign12.2/question2.py
# ['deltas', 'desalt', 'lasted', 'salted', 'staled', 'slated']
# ['resmelts', 'smelters', 'termless']
# ['retainers', 'ternaries']
# ['generating', 'greatening']