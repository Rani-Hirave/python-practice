# Exercise 12.1. Write a function called most_frequent that takes a string and prints the let-
# ters in decreasing order of frequency. Find text samples from several different languages and see
# how letter frequency varies between languages. Compare your results with the tables at http:
# // en. wikipedia. org/ wiki/ Letter_ frequencies . Solution: http: // thinkpython2.
# com/ code/ most_ frequent. py .

def most_frequent(string):
    formatted = string.replace(' ', '').lower()
    hist = dict()
    for char in formatted:
        hist[char] = hist.get(char, 0) + 1
    freq_list = list()
    for (char, freq) in hist.items():
        freq_list.append((freq, char))
    freq_list.sort(reverse=True)
    char_freq = list()
    for (freq, char) in freq_list:
        char_freq.append(char)
    print(char_freq)

print(most_frequent("Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages."))

# output
# python3 assign12.1/question1.py
# ['e', 't', 'n', 'r', 'a', 's', 'i', 'f', 'l', 'd', 'u', 'o', 'g', 'c', 'w', 'q', 'm', 'h', 'y', 'v', 'p', '.', 'x', 'k', 'b', '_']
# None