# Exercise 9.6. Write a function called is_abecedarian that returns True if the letters in a word
# appear in alphabetical order (double letters are ok). How many abecedarian words are there?
def is_abecedarian(word):
    index = 0
    while index < len(word) -1:
        if word[index] > word[index+1]:
            return False
        else:
            index +=1
    return True
    
fin = open('assign9.6/words.txt')
count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        count += 1
print('There are {} abecedarian words.'.format(count)) 

# output
# python3 assign9.6/question1.py
# There are 6 abecedarian words.