# 2. Write a function that prompts the user to input three stick lengths, converts them to integers,
# and uses is_triangle to check whether sticks with the given lengths can form a triangle.


def is_triangle(a, b, c):
    if c > (a+b) or b > (a+c) or a > (b+c):
        print('No')
    else:
        print('Yes')

def user_inputs_taringle():
    a = int(input("Please enter the length of the 1st stick:\n"))
    b = int(input("Please enter the length of the 2nd stick:\n"))
    c = int(input("Please enter the length of the 3rd stick:\n"))
    is_triangle(a,b,c)

user_inputs_taringle()
print()

# output
# python3 assign5.3/question2.py
# Please enter the length of the 1st stick:
# 1
# Please enter the length of the 2nd stick:
# 2
# Please enter the length of the 3rd stick:
# 3
# Yes