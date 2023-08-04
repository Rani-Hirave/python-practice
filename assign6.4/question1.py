# Exercise 6.4. A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
# function called is_power that takes parameters a and b and returns True if a is a power of b . Note:
# you will have to think about the base case.

def is_power(a, b):
    if a % b == 0 :
        if a == b :
            return True
    else:
        return is_power(a/b,b)
    return False

print(is_power(3,3))
print(is_power(2,4))


# output:
# python3 assign6.4/question1.py
# True
# False