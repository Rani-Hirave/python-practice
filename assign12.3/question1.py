# Exercise 12.3. Two words form a “metathesis pair” if you can transform one into the other by
# swapping two letters; for example, “converse” and “conserve”. Write a program that finds all of
# the metathesis pairs in the dictionary. Hint: don’t test all pairs of words, and don’t test all possible
# swaps. Solution: http: // thinkpython2. com/ code/ metathesis. py . Credit: This exercise
# is inspired by an example at http: // puzzlers. org .

def metathesis_pairs(d):
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    assert len(word1) == len(word2)
    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count

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

sets = anagrams('python3 assign12.3/words.txt')
print(metathesis_pairs(sets))

# output
# python3 assign12.3/question1.py
# None