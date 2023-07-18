# Exercise 3.3. Note: This exercise should be done using only the statements and other features we
# have learned so far.
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |   
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence of
# values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a
# space at the end, like this:
# print('+', end=' ')
# print('-')28
# Chapter 3. Functions
# The output of these statements is '+ -' on the same line. The output from the next print
# statement would begin on the next line.
# 2. Write a function that draws a similar grid with four rows and four columns.
def val_func1():
    print("+", 4*'-', '+', 4*'-', '+')


def val_func2():
    for x in range(4):
        print('|', 4*' ', '|', 4*' ', '|')


def output():
    val_func1()
    val_func2()
    val_func1()
    val_func2()
    val_func1()

output()

# output
# python3 assign3.1/question3.py
# + ---- + ---- +
# |      |      |
# |      |      |
# |      |      |
# |      |      |
# + ---- + ---- +
# |      |      |
# |      |      |
# |      |      |
# |      |      |
# + ---- + ---- +