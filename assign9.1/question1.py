# Exercise 9.1. Write a program that reads words.txt and prints only the words with more than 20
# characters (not counting whitespace).
fin = open('assign9.1/words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

# output
# python3 assign9.1/question1.py
# Therearesolutionstotheseexercisesin
# thenextsection.Youshouldatleastattempteach
# one before you read the solutions.