# Exercise 12.2. More anagrams!
# 3. In Scrabble a “bingo” is when you play all seven tiles in your rack, along with a letter on
# the board, to form an eight-letter word. What collection of 8 letters forms the most possible
# bingos?
# Solution: http: // thinkpython2. com/ code/ anagram_ sets. py .

fin = open("assign12.2/words.txt")

def word_to_tuple(word):
    word = tuple(sorted(word))
    return word


def print_anagrams(anagrams):
    sorted_words = list()
    for letter_set in anagrams:
        words = anagrams.get(letter_set)
        if len(words) > 1 and len(letter_set) == 8:
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
# python3 assign12.2/question3.py
# ['resmelts', 'smelters', 'termless']