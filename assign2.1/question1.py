# Repeating my advice from the previous chapter, whenever you learn a new feature,
# you should try it out in interactive mode and make errors on purpose to see what goes wrong.
# • We’ve seen that n = 42 is legal. What about 42 = n ?

n=42
print(n)

# ******************output***************
# python3 question1.py                  
# 42

# What about 42 = n ?
# 42=n
# File "<stdin>", line 1
# SyntaxError: cannot assign to literal

# • How about x = y = 1 ?
x=y=1
print(x)
print(y)
# assign value to both variable
# 1
# 1

# • In some languages every statement ends with a semi-colon, ; . What happens if you put a
# semi-colon at the end of a Python statement?
print('hello world');
n=2;
print(n);
# it print the output
# hello world
# 2

# • What if you put a period at the end of a statement?
# print('hello world').
# It gives error 
# File "<stdin>", line 1
#     print('hello world').
#                         ^
# SyntaxError: invalid syntax

# • In math notation you can multiply x and y like this: xy. What happens if you try that in
# Python?
x=2
y=5
print(xy)
# File "question1.py", line 46, in <module>
#     print(xy)
# NameError: name 'xy' is not defined