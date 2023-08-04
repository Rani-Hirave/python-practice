# Exercise 9.4. Write a function named uses_only that takes a word and a string of letters, and
# that returns True if the word contains only letters in the list. Can you make a sentence using only
# the letters acefhlo ? Other than “Hoe alfalfa”?

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True

print(uses_only('acefhlo', 'anb'))
print(uses_only('banana', 'ane'))

# output
# python3 assign9.4/question1.py
# True
# False