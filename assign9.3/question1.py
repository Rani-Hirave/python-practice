# Exercise 9.3. Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
# Write a program that prompts the user to enter a string of forbidden letters and then prints the
# number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters
# that excludes the smallest number of words?
def avoids(word, string):
    for letter in word:
        if letter in string:
            return False
    return True

string = str(input('Please enter the string of forbidden letters:\n'))

fin= open('assign9.3/words.txt')
count = 0
for word in fin:
    word = word.strip()
    if avoids(word, string):
        count += 1
        print (word)
print('The total number of words that donot contain any letter from "{}" is {}'.format(string, count))

# output:
# python3 assign9.3/question1.py
# Please enter the string of forbidden letters:
# you
# aa
# aah
# aahed
# aahing
# aahs
# aal
# aalii
# aaliis
# aals
# aardvark
# aardvarks
# aas
# aba
# The total number of words that donot contain any letter from "you" is 13