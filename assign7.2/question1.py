# Exercise 7.2. The built-in function eval takes a string and evaluates it using the Python inter-
# preter. For example:
# >>> eval('1 + 2 * 3')
# 7
# >>> import math
# >>> eval('math.sqrt(5)')
# 2.2360679774997898
# >>> eval('type(math.pi)')
# <class 'float'>
# Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
# evaluates it using eval , and prints the result.
# It should continue until the user enters 'done' , and then return the value of the last expression it
# evaluated.

import math
def eval_loop():
    while True:
        usrinput = input("enter value ")
        if eval(usrinput) == 'done':  
            break
        print(eval(usrinput))

    return eval(usrinput)

eval_loop()

# output
# python3 assign7.2/question1.py
# enter value 5
# 5
# enter value 1+2*3
# 7