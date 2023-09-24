# Exercise 10.5. Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False

# def is_sorted(t):
#     t: list
#     return t == sorted(t)
# print(is_sorted([1, 2, 2]))
# print(is_sorted(['b', 'a']))

def is_sorted(t):
    if t == sorted(t):
        return True
    return False
print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))


# python3 assign10.5/question1.py
# True
# False