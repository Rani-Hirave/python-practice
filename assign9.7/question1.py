# Exercise 9.7. This question is based on a Puzzler that was broadcast on the radio program Car
# Talk ( http: // www. cartalk. com/ content/ puzzlers ):
# Give me a word with three consecutive double letters. I’ll give you a couple of words
# that almost qualify, but don’t. For example, the word committee, c-o-m-m-i-t-t-e-e. It
# would be great except for the ‘i’ that sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-
# p-p-i. If you could take out those i’s it would work. But there is a word that has three
# consecutive pairs of letters and to the best of my knowledge this may be the only word.
# Of course there are probably 500 more but I can only think of one. What is the word?

import time

def consecutive(word):
    if word[0] == word[1] and word[2] == word[3]:
        if word[4] == word[5]:
            return word
    return False

def istripledouble(word):
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

             
def authorsolution():
    """Reads a word list and prints words with triple double letters."""
    fin = open('assign9.7/words.txt')
    for line in fin:
        word = line.strip()
        if istripledouble(word):
            print(word)  
            
def mysolution():    
    fin = open('assign9.7/words.txt')   
    for line in fin:
        word = line.strip()
        if len(word) >= 6:
            if istripledouble(word):
                print(word) 

start_time = time.time()
authorsolution()
function_time1 = time.time() - start_time
print()
start_time = time.time()
mysolution()
function_time2 = time.time() - start_time

print('Author solution {} s'.format(function_time1)) 
print('My solution {} s'.format(function_time2))   

# output
# python3 assign9.7/question1.py
# Author solution 0.0008060932159423828 s
# My solution 0.00013566017150878906 s