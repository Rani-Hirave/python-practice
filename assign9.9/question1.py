# Exercise 9.9. Here’s another Car Talk Puzzler you can solve with a search ( http: // www.
# cartalk. com/ content/ puzzlers ):
# “Recently I had a visit with my mom and we realized that the two digits that make
# up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
# wondered how often this has happened over the years but we got sidetracked with other
# topics and we never came up with an answer.
# “When I got home I figured out that the digits of our ages have been reversible six times
# so far. I also figured out that if we’re lucky it would happen again in a few years, and
# if we’re really lucky it would happen one more time after that. In other words, it would
# have happened 8 times over all. So the question is, how old am I now?”
# Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
# method zfill useful.
# Solution: http: // thinkpython2. com/ code/ cartalk3. py

def fill(i, n):
    return str(i).zfill(n)


def arereversed(i, j):
    return fill(i, 2) == fill(j, 2)[::-1]


def numinstances(diff, flag=False):
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if arereversed(daughter, mother) or arereversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def checkdiffs():
    diff = 10
    while diff < 70:
        n = numinstances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
checkdiffs()

print()
print('daughter  mother')
numinstances(18, True)

# output
# python3 assign9.9/question1.py
# diff  #instances
# 17 8
# 18 8
# 26 7
# 27 7
# 35 6
# 36 6
# 44 5
# 45 5
# 53 4
# 54 4
# 62 3
# 63 3

# daughter  mother
# 2 20
# 13 31
# 24 42
# 35 53
# 46 64
# 57 75
# 68 86
# 79 97