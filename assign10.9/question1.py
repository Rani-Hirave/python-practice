# Exercise 10.9. Write a function that reads the file words.txt and builds a list with one element
# per word. Write two versions of this function, one using the append method and the other using
# the idiom t = t + [x] . Which one takes longer to run? Why?
# Solution: http: // thinkpython2. com/ code/ wordlist. py .

import time


def make_word_list1():
    t = []
    fin = open('assign10.9/words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    t = []
    fin = open('assign10.9/words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

# python3 assign10.9/question1.py
# 19
# ['abhors', 'abidance', 'abidances', 'abide', 'abided', 'abider', 'abiders', 'abides', 'abiding', 'abied']
# 0.0008015632629394531 seconds
# 19
# ['abhors', 'abidance', 'abidances', 'abide', 'abided', 'abider', 'abiders', 'abides', 'abiding', 'abied']
# 0.00010061264038085938 seconds