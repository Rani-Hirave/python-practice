# Exercise 8.3. A string slice can take a third index that specifies the “step size”; that is, the number
# of spaces between successive characters. A step size of 2 means every other character; 3 means every
# third, etc.
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from Exercise 6.3.
def is_palindrome(string):
    string = str(string)    #one more line allows to check integers
    return string == string[::-1]

print(is_palindrome('noon'))
print(is_palindrome('no'))
print(is_palindrome(42))
print(is_palindrome(424))

# output
# python3 assign8.3/question1.py
# True
# False
# False
# True