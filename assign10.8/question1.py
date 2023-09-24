# Exercise 10.8. This exercise pertains to the so-called Birthday Paradox, which you can read about
# at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
# If there are 23 students in your class, what are the chances that two of them have the same birthday?
# You can estimate this probability by generating random samples of 23 birthdays and checking for
# matches. Hint: you can generate random birthdays with the randint function in the random
# module.
# You can download my solution from http: // thinkpython2. com/ code/ birthday. py .

import random

def has_duplicates(t):
    s = t[:]
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t


def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count

def main():
    num_students = 23
    num_simulations = 1000
    count = count_matches(num_students, num_simulations)

    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)


if __name__ == '__main__':
    main()

# python3 assign10.8/question1.py
# After 1000 simulations
# with 23 students
# there were 508 simulations with at least one match