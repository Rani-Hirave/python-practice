# Exercise 9.5. Write a function named uses_all that takes a word and a string of required letters,
# and that returns True if the word uses all the required letters at least once. How many words are
# there that use all the vowels aeiou ? How about aeiouy ?

def uses_all(word, string):
    for letter in string:
        if letter not in word:
            return False
    return True


def vowels(string):
    fin = open('assign9.5/words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if uses_all(word, string):
            count +=1
    print('There are {} words which contain all "{}" letters at once.'.format(count,string))
        
vowels('aeiou')
vowels('aeiouy')

# output
# python3 assign9.5/question1.py
# There are 3 words which contain all "aeiou" letters at once.
# There are 1 words which contain all "aeiouy" letters at once.