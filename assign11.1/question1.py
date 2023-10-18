# Exercise 11.2. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict . Solution: http: // thinkpython2. com/ code/ invert_
# dict. py .

f = open('assign11.1/words.txt')

def create_word_dict():
    word_dict = dict()
    for line in f:
        word = line.strip()
        word_dict[word] = word
    return word_dict

print(create_word_dict())

# output
# python3 assign11.1/question1.py
# {'aa': 'aa', 'aah': 'aah', 'aahed': 'aahed', 'aahing': 'aahing', 'aahs': 'aahs', 'aal': 'aal', 'aalii': 'aalii', 'aaliis': 'aaliis', 'aals': 'aals', 'aardvark': 'aardvark', 'aardvarks': 'aardvarks', 'aardwolf': 'aardwolf', 'aardwolves': 'aardwolves', 'aas': 'aas', 'aasvogel': 'aasvogel', 'aasvogels': 'aasvogels', 'aba': 'aba', 'abaca': 'abaca', 'abacas': 'abacas', 'abaci': 'abaci', 'aback': 'aback', 'abacus': 'abacus', 'abacuses': 'abacuses', 'abaft': 'abaft', 'abaka': 'abaka', 'abakas': 'abakas', 'abalone': 'abalone', 'abalones': 'abalones', 'abamp': 'abamp', 'abampere': 'abampere', 'abamperes': 'abamperes', 'abamps': 'abamps', 'abandon': 'abandon', 'abandoned': 'abandoned', 'abandoning': 'abandoning', 'abandonment': 'abandonment', 'abandonments': 'abandonments', 'abandons': 'abandons', 'abas': 'abas', 'abase': 'abase', 'abased': 'abased', 'abasedly': 'abasedly', 'abasement': 'abasement', 'abasements': 'abasements', 'abaser': 'abaser', 'abasers': 'abasers', 'abases': 'abases', 'abash': 'abash', 'abashed': 'abashed', 'abashes': 'abashes', 'abashing': 'abashing', 'abasing': 'abasing', 'abatable': 'abatable', 'abate': 'abate', 'abated': 'abated', 'abatement': 'abatement', 'abatements': 'abatements', 'abater': 'abater', 'abaters': 'abaters', 'abates': 'abates', 'shoe': 'shoe', 'cold': 'cold', 'schooled': 'schooled', 'interlock': 'interlock'}