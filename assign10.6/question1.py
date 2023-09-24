# Exercise 10.6. Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False
print(is_anagram("listen", "silent"))
print(is_anagram("bad", "dad"))


# python3 assign10.6/question1.py
# True
# False