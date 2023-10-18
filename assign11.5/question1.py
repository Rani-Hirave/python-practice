# Exercise 11.5. Two words are “rotate pairs” if you can rotate one of them and get the other (see
# rotate_word in Exercise 8.5).
# Write a program that reads a wordlist and finds all the rotate pairs. Solution: http: //
# thinkpython2. com/ code/ rotate_ pairs. py

def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

def make_word_dict():
    d = dict()
    fin = open('assign11.5/words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    return d


def rotate_pairs(word, word_dict):
    for i in range(1, 27):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)

word_dict = make_word_dict()
for word in word_dict:
    rotate_pairs(word, word_dict)

# output
# python3 assign11.5/question1.py
# aa 26 aa
# aah 26 aah
# aahed 26 aahed
# aahing 26 aahing
# aahs 26 aahs
# aal 26 aal
# aalii 26 aalii
# aaliis 26 aaliis
# aals 26 aals
# aardvark 26 aardvark
# aardvarks 26 aardvarks
# aardwolf 26 aardwolf
# aardwolves 26 aardwolves
# aas 26 aas
# aasvogel 26 aasvogel
# aasvogels 26 aasvogels
# aba 26 aba
# abaca 26 abaca
# abacas 26 abacas
# abaci 26 abaci
# aback 26 aback
# abacus 26 abacus
# abacuses 26 abacuses
# abaft 26 abaft
# abaka 26 abaka
# abakas 26 abakas
# abalone 26 abalone
# abalones 26 abalones
# abamp 26 abamp
# abampere 26 abampere
# abamperes 26 abamperes
# abamps 26 abamps
# abandon 26 abandon
# abandoned 26 abandoned
# abandoning 26 abandoning
# abandonment 26 abandonment
# abandonments 26 abandonments
# abandons 26 abandons
# abas 26 abas
# abase 26 abase
# abased 26 abased
# abasedly 26 abasedly
# abasement 26 abasement
# abasements 26 abasements
# abaser 26 abaser
# abasers 26 abasers
# abases 26 abases
# abash 26 abash
# abashed 26 abashed
# abashes 26 abashes
# abashing 26 abashing
# abasing 26 abasing
# abatable 26 abatable
# abate 26 abate
# abated 26 abated
# abatement 26 abatement
# abatements 26 abatements
# abater 26 abater
# abaters 26 abaters
# abates 26 abates
# shoe 26 shoe
# cold 26 cold
# schooled 26 schooled
# interlock 26 interlock